from django.urls import path
from . import views

urlpatterns = [
    # Pastikan merujuk ke views.contacts
    path('', views.contacts, name='contacts'),
]