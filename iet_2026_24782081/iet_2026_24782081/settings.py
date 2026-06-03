import os
from pathlib import Path

# Base directory dari project Django
BASE_DIR = Path(__file__).resolve().parent.parent

# Pengaturan Keamanan Utama
SECRET_KEY = 'django-insecure-ubah-ini-sesuai-kebutuhan-proyek-kamu'
DEBUG = True
ALLOWED_HOSTS = []

# ==============================================================================
# DAFTAR APLIKASI (INSTALLED APPS) - UTUH & LENGKAP
# ==============================================================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Aplikasi CRUD Laporan Kota (Lab 5 - Tetap Utuh)
    'main_app',

    # Aplikasi Manajemen User (Lab 6)
    'usermanagement_24782081', 
]

# ==============================================================================
# MIDDLEWARE - UTUH
# ==============================================================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'iet_2026_24782081.urls'

# ==============================================================================
# CONFIGURASI TEMPLATES - UTUH (Mendukung Folder Utama)
# ==============================================================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'iet_2026_24782081.wsgi.application'

# ==============================================================================
# DATABASE CONFIGURATION - UTUH
# ==============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ==============================================================================
# PASSWORD VALIDATORS - UTUH BANYAK BARISNYA
# ==============================================================================
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internasionalisasi dan Waktu
LANGUAGE_CODE = 'id-id'
TIME_ZONE = 'Asia/Jakarta'
USE_I18N = True
USE_TZ = True

# Static Files
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ==============================================================================
# KONFIGURASI TAMBAHAN LAB 6 (YANG BARU DIMASUKKAN DI PALING BAWAH)
# ==============================================================================
AUTH_USER_MODEL = 'usermanagement_24782081.User'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'custom_login'