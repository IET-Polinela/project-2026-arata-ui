"""
iet_2026_24782081 URL Configuration
==============================================================================
Rute URL Utama - Pembenahan Konflik Jalur Login / HTTP 405 Fix
==============================================================================
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 1. Administrasi Django
    path('admin/', admin.site.urls),

    # 2. Aplikasi Autentikasi didahulukan agar mengeliminasi bentrokan rute kosong ''
    path('', include('usermanagement_24782081.urls')),

    # 3. Aplikasi Dashboard Statistik (Lab 7)
    path('dashboard/', include('dashboard_24782081.urls')),

    # 4. Aplikasi CRUD Laporan Warga (Lab 5) diletakkan paling bawah
    path('', include('main_app.urls')),
]