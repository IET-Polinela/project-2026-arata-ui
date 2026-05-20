from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Report

# 1. Menampilkan Daftar Laporan (Read All)
class ReportListView(ListView):
    model = Report
    template_name = 'main_app/home.html'
    context_object_name = 'reports'
    ordering = ['-created_at'] # Mengurutkan dari yang terbaru

# 2. Menampilkan Detail Laporan (Read Single Data)
class ReportDetailView(DetailView):
    model = Report
    template_name = 'main_app/report_detail.html'
    context_object_name = 'report'

# 3. Membuat Laporan Baru (Create)
class ReportCreateView(CreateView):
    model = Report
    fields = ['title', 'category', 'description', 'location']
    template_name = 'main_app/add_report.html'
    success_url = reverse_lazy('report_list') # Redirect ke halaman utama jika sukses

# 4. Mengedit Data Laporan (Update)
class ReportUpdateView(UpdateView):
    model = Report
    fields = ['title', 'category', 'description', 'location']
    template_name = 'main_app/add_report.html' # Memakai template yang sama dengan create
    success_url = reverse_lazy('report_list')

# 5. Menghapus Laporan (Delete)
class ReportDeleteView(DeleteView):
    model = Report
    template_name = 'main_app/report_confirm_delete.html'
    success_url = reverse_lazy('report_list')

# 6. View Khusus Workflow Perubahan Status Laporan
class ReportUpdateStatusView(View):
    def post(self, request, pk):
        report = get_object_or_404(Report, pk=pk)
        new_status = request.POST.get('status')
        report.status = new_status
        report.save()
        return redirect('report_list') # Kembali ke halaman utama setelah ganti status