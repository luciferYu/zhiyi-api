# -*- coding: utf-8 -*-
# @Time    : 2022/12/8 15:00
# @Author  : YuZhiYi
# @Email   : 
# @Software : zhiyi-api
import os

ENV = os.environ.get('ENV', 'test')

if ENV.lower() in ['pro', 'prod']:
    from .pro import *
else:
    from .test import *