import os
from re import DEBUG

from storefront.settings.dev import SECRET_KEY
from .common import *

DEBUG = False

SECRET_KEY = os.env['SECRET_KEY']

ALLOWED_HOSTS = []
