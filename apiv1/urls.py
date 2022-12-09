# -*- coding: utf-8 -*-
# @Time    : 2022/12/8 14:18
# @Author  : YuZhiYi
# @Email   : 
# @Software : zhiyi-api
# -*- coding: utf-8 -*-
# @Time    : 2022/12/8 13:21
# @Author  : YuZhiYi
# @Email   :
# @Software : zhiyi-api
app_name = 'apiv1'
from django.urls import path, re_path
from apiv1.user.views import (
    UserViewSet
    , GroupViewSet
)

urlpatterns = [
    re_path('user/$', UserViewSet.as_view({'get': 'list'})),
    re_path('user/(?P<id>[0-9]+)/$', UserViewSet.as_view({'get': 'retrieve'})),
    re_path('group/$', GroupViewSet.as_view({'get': 'list'}))
]