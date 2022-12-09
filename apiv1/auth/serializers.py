# -*- coding: utf-8 -*-
# @Time    : 2022/12/8 13:25
# @Author  : YuZhiYi
# @Email   : 
# @Software : zhiyi-api
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']

# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=150)
#     password = serializers.CharField(max_length=150)


class ZhiyiTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        token['user_id'] = user.id
        token['is_superuser'] = user.is_superuser
        token['is_active'] = user.is_active
        token['is_staff'] = user.is_staff
        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        return token
