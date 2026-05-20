from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Report

# 1. Tampilan Daftar Laporan
class ReportListView(ListView):
    model = Report
    template_name = 'main_app/home.html'
    context_object_name = 'reports'
    ordering = ['-created_at']

# 2. Detail Laporan
class ReportDetailView(DetailView):
    model = Report
    template_name = 'main_app/report_detail.html'
    context_object_name = 'report'

# 3. Tambah Laporan Baru (Menggunakan SuccessMessageMixin untuk Feedback)
class ReportCreateView(SuccessMessageMixin, CreateView):
    model = Report
    fields = ['title', 'category', 'description', 'location']
    template_name = 'main_app/add_report.html'
    success_url = reverse_lazy('report_list')
    success_message = "Laporan baru berhasil ditambahkan ke dalam sistem!" # Notifikasi sukses

# 4. Edit Laporan (Menggunakan SuccessMessageMixin)
class ReportUpdateView(SuccessMessageMixin, UpdateView):
    model = Report
    fields = ['title', 'category', 'description', 'location']
    template_name = 'main_app/add_report.html'
    success_url = reverse_lazy('report_list')
    success_message = "Data laporan berhasil diperbarui!"

# 5. Hapus Laporan
class ReportDeleteView(DeleteView):
    model = Report
    template_name = 'main_app/report_confirm_delete.html'
    success_url = reverse_lazy('report_list')
    
    # Custom method untuk memunculkan pesan setelah berhasil menghapus
    def delete(self, request, *args, **kwargs):
        # Gunakan messages.success (tidak ada messages.danger di Django)
        messages.success(self.request, "Laporan telah berhasil dihapus dari sistem.")
        return super().delete(request, *args, **kwargs)

# 6. Alur Kerja Perubahan Status Workflow dengan Pesan Info
class ReportUpdateStatusView(View):
    def post(self, request, pk):
        report = get_object_or_404(Report, pk=pk)
        old_status = report.status
        new_status = request.POST.get('status')
        report.status = new_status
        report.save()
        
        messages.info(request, f"Status laporan '{report.title}' berhasil diubah menjadi {new_status}.")
        return redirect('report_list')