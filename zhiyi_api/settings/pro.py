# -*- coding: utf-8 -*-
# @Time    : 2022/12/8 15:02
# @Author  : YuZhiYi
# @Email   : 
# @Software : zhiyi-api
from .base import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!3669!+y&fyo9w6(52xx!%281j$k)mxvf5+vvxc*v@kpu&f)=n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}