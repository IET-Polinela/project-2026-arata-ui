from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Jalur bawaan admin panel Django
    path('admin/', admin.site.urls),
    
    # Menghubungkan rute utama langsung ke berkas urls milik main_app
    path('', include('main_app.urls')),
]