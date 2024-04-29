from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2!ccrcwxv3wq_4j+cn*-t)(h^f7p84)7x9581&^8m@&(9i&uwp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'paypal.standard.ipn',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',  
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gbeduboss',
    'beats',
    'beatcart',
    'ckeditor',
    'ckeditor_uploader',
    'taggit',
    'embed_video', 
    'guest_user',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gbedufolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'gbeduboss.context_processor.cartpros',
                # 'gbeduboss.context_processor.cart',
                # 'gbeduboss.context_processor.remove_item',
            ],
        },
    },
]

WSGI_APPLICATION = 'gbedufolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'gbeduboss/static')]


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'my_uploads')



####################################
    ##  CKEDITOR CONFIGURATION ##
####################################
# for uploading images and the rest using ckeditor
# https://django-ckeditor.readthedocs.io/en/latest/

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"


CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 'auto',
    },
}

###################################
    ##  TAG CASE SENSITIVE ##
#################################### 
TAGGIT_CASE_INSENSITIVE = True




# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# ####################### FOR DJANGO GUEST USER ######################### #
AUTHENTICATION_BACKENDS = [
   "django.contrib.auth.backends.ModelBackend",
   # it should be the last entry to prevent unauthorized access
   "guest_user.backends.GuestBackend",
]

GUEST_USER_NAME_GENERATOR = "guest_user.functions.generate_numbered_username"
# class AppSettings(GUEST_USER_NAME_GENERATOR):
#     "guest_user.functions.generate_numbered_username"


# GUEST_USER_NAME_PREFIX = "generate_numbered_username"


###############   EMAIL SETTINGS ###################
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS= True
EMAIL_HOST= 'smtp.gmail.com'
EMAIL_HOST_USER= 'phlenfy28@gmail.com'
EMAIL_HOST_PASSWORD= 'lcegzbzpglrpwqpw.'
EMAIL_PORT= 587


###############   PAYPAL SETTINGS ###################
PAYPAL_TEST = False

PAYPAL_RECEIVER_EMAIL = 'olajidemeshe@gmail.com'



###############   JAZZMIN SETTINGS ###################
JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "GBEDUBOSS Admin",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "GBEDUBOSS EMPIRE",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "GBEDUBOSS",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "images/gbedu.jpg",

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": "images/gbedu.jpg",

    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": "images/gbedu.jpg",

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,

    # Welcome text on the login screen
    "welcome_sign": "Welcome to GBEDUBOSS EMPIRE",

    # Copyright on the footer
    "copyright": "Acme GBEDUBOSS EMPIRE Ltd",

    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "auth.User",

    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": 'image',
}