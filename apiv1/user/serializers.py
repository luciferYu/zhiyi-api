# -*- coding: utf-8 -*-
# @Time    : 2022/12/8 13:25
# @Author  : YuZhiYi
# @Email   : 
# @Software : zhiyi-api
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin


class UserSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = User
        # fields = '__all__'
        exclude = ['password']


class GroupSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Group
        #fields = ['name']
