from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from django.contrib.auth import authenticate
from loguru import logger
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (
    ZhiyiTokenObtainPairSerializer
)





class ZhiyiTokenObtainPairView(TokenObtainPairView):
    serializer_class = ZhiyiTokenObtainPairSerializer
