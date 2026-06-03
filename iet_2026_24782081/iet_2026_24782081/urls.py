from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rute Autentikasi Utama (Diprioritaskan di atas)
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='custom_login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='custom_login'), name='custom_logout'),
    
    # Rute Manajemen Laporan Kota
    path('', include('main_app.urls')),
]