"""
usermanagement_24782081 URL Configuration
==============================================================================
Rute Autentikasi Pengguna (Lab 6)
==============================================================================
"""
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Jalur login resmi mengarah langsung ke template login.html
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='custom_login'),
    
    # Jalur logout resmi kembali melemparkan user ke halaman login setelah keluar
    path('logout/', auth_views.LogoutView.as_view(next_page='custom_login'), name='custom_logout'),
]