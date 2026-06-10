"""
dashboard_24782081 URL Configuration
==============================================================================
Rute URL Internal Khusus Menu Dashboard & API Endpoint (Lab 7)
==============================================================================
"""
from django.urls import path
from .views import DashboardIndexView, dashboard_stats_api, dashboard_search_api

app_name = 'dashboard'

urlpatterns = [
    # 1. Halaman Utama Dashboard (Merender HTML Template)
    path('', DashboardIndexView.as_view(), name='index'),

    # 2. Endpoint API JSON untuk Distribusi Grafik Chart.js & Tabel 5 Terkini
    path('api/stats/', dashboard_stats_api, name='api_stats'),

    # 3. Endpoint API JSON untuk Fitur Live Search & Pengambilan Detail Modal Pop-up
    path('api/search/', dashboard_search_api, name='api_search'),
]