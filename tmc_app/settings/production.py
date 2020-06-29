#Settings para producción
from .base import *
import dj_database_url
DEBUG= False
CSRF_COOKIE_SECURE=True # Solo permite enviar CSRF a traves de conexión HTTPS
X_FRAME_OPTIONS='DENY'
SECURE_CONTENT_TYPE_NOSNIFF=True
SECURE_BROWSER_XSS_FILTER=True
SESSION_COOKIE_SECURE=True #Solo permite iniciar session solo con HTTPS
SECURE_SSL_REDIRECT=True
ALLOWED_HOSTS = ['tmcs-app.herokuapp.com']
SECRET_KEY = os.environ.get('SECRET_KEY')

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware',]

DATABASES = {
    'default': dj_database_url.config(
        default= os.environ.get('DATABASE_URL')
    )
}
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'