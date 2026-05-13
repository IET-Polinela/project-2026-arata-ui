from django.urls import path
from . import views

urlpatterns = [
    # Ubah views.home menjadi views.about
    path('', views.about, name='about'), 
]