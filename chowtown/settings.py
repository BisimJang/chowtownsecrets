import os
from datetime import timedelta
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# =====================================
# 🔧 BASE CONFIGURATION
# =====================================
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = True
# DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')


# =====================================
# 📦 INSTALLED APPS
# =====================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # Third-party apps
    'corsheaders',

    'rest_framework',
    'rest_framework.authtoken',

    'rest_framework_simplejwt',
    'drf_yasg',
    'dj_rest_auth',
    'dj_rest_auth.registration',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # Local apps
    'accounts',
    'recipes',
]


# =====================================
# 🧱 MIDDLEWARE
# =====================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Keep this second
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # Make sure this is last
]


# =====================================
# 🛠 TEMPLATES
# =====================================
ROOT_URLCONF = 'chowtown.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'chowtown.wsgi.application'

# =====================================
# 🗄 DATABASE CONFIGURATION
# =====================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}




# =====================================
# 🔐 PASSWORD VALIDATION
# =====================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# =====================================
# 🌍 INTERNATIONALIZATION
# =====================================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# =====================================
# 🧾 STATIC & MEDIA FILES
# =====================================
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# =====================================
# 🔄 CORS
# =====================================
CORS_ALLOW_ALL_ORIGINS = True

# =====================================
# 🔐 AUTH & REDIRECTION
# =====================================
LOGOUT_REDIRECT_URL = '/recipes/recipes-home'  # fixed leading slash

# =====================================
# 🔧 DEFAULT FIELD TYPE
# =====================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# =====================================
# JWT authentication settings
# =====================================
SITE_ID = 1

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'auth',
    'JWT_AUTH_REFRESH_COOKIE': 'refresh',
    'JWT_AUTH_RETURN_EXPIRATION': True,

}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "AUTH_HEADER_TYPES": ("Bearer",),
}

# Email settings for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# AllAuth email settings
ACCOUNT_EMAIL_VERIFICATION = 'none'  # Options: 'mandatory', 'optional', or 'none'
ACCOUNT_EMAIL_REQUIRED = True

# If you want to disable email verification temporarily during development
ACCOUNT_EMAIL_VERIFICATION = 'none'


SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
}
ACCOUNT_SIGNUP_FIELDS = ['username*', 'password1*', 'password2*']
