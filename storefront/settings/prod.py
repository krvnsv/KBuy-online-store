import os

from storefront.settings.dev import SECRET_KEY
from .common import *

DEBUG = False

SECRET_KEY = os.env['SECRET_KEY']

ALLOWED_HOSTS = ['kbuy-prod-10f4d2f1e438.herokuapp.com']
