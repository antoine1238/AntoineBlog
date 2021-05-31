from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["antoineblog.herokuapp.com"]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "d7kkn6ogdt9e2f",
        'USER': "lvuldvmusdvkfb",
        'PASSWORD': "a54e1c2d0b1df4c6dc5886f760cc4b416d3dc77421558c26d7801642d2aee6eb",
        'HOST': "ec2-34-193-113-223.compute-1.amazonaws.com",
        "PORT": 5432,
    }
}

STATIC_ROOT = os.path.join(BASE_DIR,"staticfiles")
# STATIC_ROOT = '/static/'
