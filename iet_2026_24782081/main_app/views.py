from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View, TemplateView
from .models import Report  
from .forms import ReportForm  

# 1. Halaman Dashboard Utama (Membaca templates/report_list.html)
class ReportListView(ListView):
    model = Report
    template_name = 'report_list.html'  
    context_object_name = 'reports'

# 2. Halaman Detail Laporan (Membaca templates/report_detail.html)
class ReportDetailView(DetailView):
    model = Report
    template_name = 'report_detail.html'

# 3. Halaman Tambah Laporan Baru (Membaca templates/report_form.html)
class ReportCreateView(CreateView):
    model = Report
    form_class = ReportForm
    template_name = 'report_form.html'
    success_url = reverse_lazy('report_list')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('custom_login')
        
        # PENGATURAN LOGIKA YANG BENAR:
        # Jika user yang masuk BUKAN admin DAN BUKAN superuser, maka akses ditolak!
        if not (getattr(request.user, 'is_admin', False) or request.user.is_superuser):
            messages.error(request, "⚠️ Akses Ditolak! Anda bukan pengguna otoritas (Admin).")
            return redirect('/')
            
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Laporan baru berhasil ditambahkan ke dalam sistem!")
        return super().form_valid(form)

# 4. Halaman Edit Laporan (Membaca templates/report_form.html)
class ReportUpdateView(UpdateView):
    model = Report
    form_class = ReportForm
    template_name = 'report_form.html'
    success_url = reverse_lazy('report_list')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('custom_login')
        if not (getattr(request.user, 'is_admin', False) or request.user.is_superuser):
            messages.error(request, "⚠️ Akses Ditolak! Anda bukan pengguna otoritas (Admin).")
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Data laporan berhasil diperbarui!")
        return super().form_valid(form)

# 5. Halaman Konfirmasi Hapus (Membaca templates/report_confirm_delete.html)
class ReportDeleteView(DeleteView):
    model = Report
    template_name = 'report_confirm_delete.html'
    success_url = reverse_lazy('report_list')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('custom_login')
        if not (getattr(request.user, 'is_admin', False) or request.user.is_superuser):
            messages.error(request, "⚠️ Akses Ditolak! Anda bukan pengguna otoritas (Admin).")
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.error(self.request, "Data laporan telah berhasil dihapus dari sistem.")
        return super().delete(request, *args, **kwargs)

# 6. Alur Kerja Perubahan Status / Workflow Tombol
class ReportUpdateStatusView(View):
    def post(self, request, pk):
        if not request.user.is_authenticated:
            return redirect('custom_login')
        if not (getattr(request.user, 'is_admin', False) or request.user.is_superuser):
            messages.error(request, "⚠️ Akses Ditolak! Anda bukan pengguna otoritas (Admin).")
            return redirect('/')

        report = get_object_or_404(Report, pk=pk)
        action = request.POST.get('action')
        
        if action == 'verify' and report.status == 'Reported':
            report.status = 'Verified'
            messages.info(request, f"Status laporan '{report.title}' kini diubah menjadi Verified.")
        elif action == 'resolve' and report.status == 'Verified':
            report.status = 'Resolved'
            messages.success(request, f"Status laporan '{report.title}' kini diubah menjadi Resolved.")
        
        report.save()
        return redirect('report_list')

# 7. Tampilan Halaman Login Mandiri (Membaca templates/login.html)
class CustomLoginView(TemplateView):
    template_name = 'login.html'