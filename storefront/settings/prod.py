import os
from storefront.settings.dev import SECRET_KEY
import dj_database_url
from .common import *

DEBUG = False

SECRET_KEY = os.env['SECRET_KEY']

ALLOWED_HOSTS = ['kbuy-prod-10f4d2f1e438.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config()
}