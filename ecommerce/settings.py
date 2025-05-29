import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Dossiers templates et static
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')  # /chemin/vers/projet/templates
STATIC_DIR = os.path.join(BASE_DIR, 'static')        # /chemin/vers/projet/static

# Sécurité
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "unsafe-secret-key-dev")  # Remplacer en prod !
DEBUG = os.environ.get("DEBUG", "True") == "True"
ALLOWED_HOSTS = ['*']  # À adapter en production

# Applications installées
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop',  # Ton app principale
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # <- Virgule ajoutée ici
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# URLs principales
ROOT_URLCONF = 'ecommerce.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Ici on pointe directement vers le dossier templates
        'DIRS': [TEMPLATES_DIR],  
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Important pour auth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Tes context processors perso, si tu les utilises :
                'shop.context_processors.cart_count',
                'shop.context_processors.categories_context',
            ],
        },
    },
]

# WSGI
WSGI_APPLICATION = 'ecommerce.wsgi.application'

# Base de données SQLite simple
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validation des mots de passe
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Localisation
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'

# Fichiers statiques (CSS, JS, images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR]  # dossiers à utiliser en dev
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # dossier de collecte statics en prod
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Fichiers médias (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Clé auto-incrément Django par défaut
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
