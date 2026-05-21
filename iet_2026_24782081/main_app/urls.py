from django.urls import path
from . import views

urlpatterns = [
    # Halaman dashboard utama (http://127.0.0.1:8000/)
    path('', views.ReportListView.as_view(), name='report_list'),
    
    # Jalur fungsionalitas aplikasi
    path('report/<int:pk>/', views.ReportDetailView.as_view(), name='report_detail'),
    path('add/', views.ReportCreateView.as_view(), name='add_report'),
    path('report/<int:pk>/edit/', views.ReportUpdateView.as_view(), name='edit_report'),
    path('report/<int:pk>/delete/', views.ReportDeleteView.as_view(), name='delete_report'),
    path('report/<int:pk>/status/', views.ReportUpdateStatusView.as_view(), name='update_status'),
    
    # Jalur menu halaman login khusus (http://127.0.0.1:8000/login/)
    path('login/', views.CustomLoginView.as_view(), name='custom_login'),
]