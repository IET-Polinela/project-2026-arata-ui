from django.shortcuts import render, redirect
from .models import Report
from .forms import ReportForm # Pastikan kamu sudah membuat forms.py juga

def home(request):
    reports = Report.objects.all()
    # Tambahkan 'main_app/' sebelum 'home.html'
    return render(request, 'main_app/home.html', {'reports': reports})

# PASTIKAN NAMA FUNGSI INI ADALAH 'add_report' (semua huruf kecil)
def add_report(request):
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReportForm()
    return render(request, 'main_app/add_report.html', {'form': form})