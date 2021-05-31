from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["antoineblog.herokuapp.com"]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "daolnd94o67hai",
        'USER': "qjwvmnzhruvqoh",
        'PASSWORD': "b49c5735daa062fb72fde101149ac1aa2dce5e47d61f5101ae0fbc2e72eae6ed",
        'HOST': "ec2-18-214-208-89.compute-1.amazonaws.com",
        "PORT": 5432,
    }
}

# STATIC_ROOT = os.path.join(BASE_DIR,"staticfiles")
STATIC_ROOT = '/static/'
