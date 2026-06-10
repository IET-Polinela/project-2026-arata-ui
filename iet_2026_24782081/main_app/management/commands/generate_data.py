import random
from django.core.management.base import BaseCommand
from faker import Faker
from main_app.models import Report  # Memastikan impor model Report dari main_app

class Command(BaseCommand):
    help = 'Generate contextual fake reports for Smart City Dashboard'

    def add_arguments(self, parser):
        # Argumen untuk menentukan jumlah data yang ingin di-generate
        parser.add_argument('num_records', type=int, help='Jumlah data laporan yang akan dibuat')

    def handle(self, *args, **kwargs):
        num_records = kwargs['num_records']
        
        # Inisialisasi Faker dengan lokalisasi Bahasa Indonesia agar data alamat & kota lokal
        fake = Faker('id_ID')

        # Mapping Kategori dengan judul dan deskripsi yang relevan sesuai modul halaman 2
        context_data = {
            'Jalan Rusak': {
                'titles': [
                    'Lubang Besar di Tengah Jalan', 
                    'Aspal Mengelupas Parah', 
                    'Jalan Bergelombang Bahayakan Motor', 
                    'Ambles di Dekat Drainase'
                ],
                'desc': 'Ditemukan kerusakan jalan yang cukup dalam. Mohon segera diperbaiki sebelum memakan korban jiwa atau merusak kendaraan warga.'
            },
            'Sampah': {
                'titles': [
                    'Tumpukan Sampah Liar', 
                    'Bau Menyengat Sampah Menumpuk', 
                    'TPS Melebihi Kapasitas', 
                    'Sampah Menutup Saluran Air'
                ],
                'desc': 'Warga mengeluhkan penumpukan sampah yang belum diangkut selama lebih dari 3 hari. Bau mulai menyengat dan mengganggu aktivitas.'
            },
            'Lampu Mati': {
                'titles': [
                    'Penerangan Jalan Umum Mati', 
                    'Lampu Jalan Berkedip', 
                    'Kabel Lampu Putus', 
                    'Area Gelap Rawan Kriminalitas'
                ],
                'desc': 'Lampu jalan di area ini mati total sejak kemarin malam. Kondisi jalan menjadi gelap gulita dan membahayakan pengguna jalan.'
            },
            'Drainase': {
                'titles': [
                    'Saluran Air Mampet', 
                    'Drainase Meluap Saat Hujan', 
                    'Tutup Got Pecah', 
                    'Penyumbatan Karena Sedimen'
                ],
                'desc': 'Saluran air tersumbat sehingga setiap kali hujan turun, air meluap ke badan jalan dan masuk ke teras rumah warga sekitar.'
            },
            'Keamanan': {
                'titles': [
                    'Aksi Vandalisme Fasilitas Umum', 
                    'Pencurian Kabel Telepon', 
                    'Laporan Kerumunan Mencurigakan', 
                    'Gangguan Ketertiban Umum'
                ],
                'desc': 'Dibutuhkan patroli tambahan di area ini karena laporan warga terkait aktivitas yang mencurigakan pada jam malam.'
            }
        }

        # Pilihan status laporan yang tersedia
        status_choices = ['REPORTED', 'VERIFIED', 'IN PROGRESS', 'RESOLVED']

        self.stdout.write(self.style.WARNING(f'Sedang membuat {num_records} data laporan... Mohon tunggu.'))

        # Loop untuk membuat data ke dalam database
        for _ in range(num_records):
            # Pilih kategori secara acak dari keys context_data
            category = random.choice(list(context_data.keys()))
            
            # Ambil template judul dan deskripsi berdasarkan kategori yang terpilih
            title_template = random.choice(context_data[category]['titles'])
            description_base = context_data[category]['desc']

            # Pembuatan data laporan menggunakan Django ORM ke database
            Report.objects.create(
                # Judul ditambah nama jalan random agar unik
                title=f"{title_template} - {fake.street_name()}",
                category=category,
                # Deskripsi ditambah detail lokasi dari faker
                description=f"{description_base} Lokasi detail: {fake.street_address()}.",
                location=f"Kecamatan {fake.city()}, {fake.address()}",
                status=random.choice(status_choices)
            )

        # Menampilkan pesan sukses di terminal jika berhasil
        self.stdout.write(self.style.SUCCESS(f'Berhasil membuat {num_records} laporan yang kontekstual!'))