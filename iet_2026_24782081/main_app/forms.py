from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        # Field ini harus sesuai dengan yang ada di models.py kamu
        fields = ['title', 'description', 'location']
        
        # Bagian ini yang bikin tampilan input jadi modern (Bootstrap)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan judul laporan...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Ceritakan detail laporannya...'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Contoh: Kec. Kemiling, Bandar Lampung'
            }),
        }
        
        # Label untuk mempercantik nama field di browser
        labels = {
            'title': 'Judul Laporan',
            'description': 'Deskripsi Masalah',
            'location': 'Lokasi Kejadian',
        }