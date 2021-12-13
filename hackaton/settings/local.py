from hackaton.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "postgres_hackaton",
        "PORT": 5432,
        "DISABLE_SERVER_SIDE_CURSORS": True,
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, "admin_interface/public/media/")
MEDIA_URL = "/media/"
