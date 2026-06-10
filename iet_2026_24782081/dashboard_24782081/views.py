from django.views.generic import TemplateView
from django.http import JsonResponse
from django.db.models import Count
from main_app.models import Report  # Mengambil model Report dari main_app

class DashboardIndexView(TemplateView):
    """
    View utama untuk merender halaman dashboard statis.
    Grafik dan tabel di dalamnya akan diisi secara asinkron menggunakan Fetch API.
    """
    template_name = 'dashboard/index.html'


def dashboard_stats_api(request):
    """
    API Endpoint yang mengembalikan data statistik dalam format JSON.
    Donsumsi oleh Chart.js dan komponen list di frontend.
    """
    # 1. Agregasi Distribusi Kategori (Menghitung jumlah laporan per kategori)
    category_data = Report.objects.values('category').annotate(total=Count('id'))
    category_distribution = {item['category']: item['total'] for item in category_data}

    # 2. Agregasi Distribusi Status (Menghitung jumlah laporan per status progres)
    status_data = Report.objects.values('status').annotate(total=Count('id'))
    status_distribution = {item['status']: item['total'] for item in status_data}

    # 3. Mengambil 5 Laporan Masuk Terbaru (Status: REPORTED)
    recent_reported = Report.objects.filter(status='REPORTED').order_by('-id')[:5]
    recent_reported_list = [
        {
            'id': r.id,
            'title': r.title,
            'location': r.location,
            'category': r.category
        } for r in recent_reported
    ]

    # 4. Mengambil 5 Laporan Selesai Terbaru (Status: RESOLVED)
    recent_resolved = Report.objects.filter(status='RESOLVED').order_by('-id')[:5]
    recent_resolved_list = [
        {
            'id': r.id,
            'title': r.title,
            'location': r.location,
            'category': r.category
        } for r in recent_resolved
    ]

    # Menyusun semua data ke dalam satu dictionary besar
    data = {
        'category_distribution': category_distribution,
        'status_distribution': status_distribution,
        'recent_reported': recent_reported_list,
        'recent_resolved': recent_resolved_list,
    }

    return JsonResponse(data)


def dashboard_search_api(request):
    """
    API Endpoint untuk fitur Live Search instan dan Detail Modal Pop-up.
    """
    report_id = request.GET.get('id')
    
    # JIKA REQUEST MEMILIKI PARAMETER 'id': Kembalikan detail 1 data spesifik (untuk Modal)
    if report_id:
        try:
            report = Report.objects.get(id=report_id)
            return JsonResponse({
                'id': report.id,
                'title': report.title,
                'category': report.category,
                'description': report.description,
                'location': report.location,
                'status': report.get_status_display(), # Mengambil string readable dari pilihan status
                'created_at': report.id # Menggunakan ID atau fallback representation sederhana
            })
        except Report.DoesNotExist:
            return JsonResponse({'error': 'Data laporan tidak ditemukan'}, status=404)

    # JIKA REQUEST BIASA / LIVE SEARCH: Lakukan pemfilteran data berdasarkan kata kunci 'q'
    query = request.GET.get('q', '')
    if query:
        # Mencari kesamaan kata kunci pada Judul, Kategori, atau Lokasi
        reports = Report.objects.filter(
            title__icontains=query
        ) | Report.objects.filter(
            category__icontains=query
        ) | Report.objects.filter(
            location__icontains=query
        )
        reports = reports.order_by('-id')[:20]  # Batasi maksimal 20 hasil demi efisiensi
    else:
        # Jika kolom pencarian kosong, tampilkan 10 data teratas secara default
        reports = Report.objects.order_by('-id')[:10]

    reports_list = [
        {
            'id': r.id,
            'title': r.title,
            'category': r.category,
            'location': r.location,
            'status': r.get_status_display()
        } for r in reports
    ]

    return JsonResponse({'reports': reports_list})