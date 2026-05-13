from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')), # Hanya di sini boleh pakai include
    path('about/', include('about.urls')),
    path('contacts/', include('contacts.urls')),
]