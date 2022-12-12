# -*- coding: utf-8 -*-
# @Time    : 2022/12/12 11:06
# @Author  : YuZhiYi
# @Email   : 
# @Software : zhiyi-api
from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from apiv1.user.models import (
    Role,
    Menu
)

@admin.register(Menu)
class MenuAdmin(DjangoMpttAdmin):
    fields = [
        'name',
        'parent',
        'desc',
        'status'
    ]

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    fields = [
        'role_name',
        'role_desc',
        'users',
        'groups',
        'menus',
        'permissions',
        'status',
    ]