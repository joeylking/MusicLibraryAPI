# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-q=#koaoyj%lfuj1&x68!x=%09x7axvymwgfjnk1p6axc_d_5_$'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_libary_database',
        'USER': 'root',
        'PASSWORD': 'eifh0sdjfs-275d',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}