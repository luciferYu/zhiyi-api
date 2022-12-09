from loguru import logger
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from libs.ZhiyiRestViews.ZhiyiAbstractViewSet import ZhiyiAbstractModelViewSet
from .serializers import (
    UserSerializer
    , GroupSerializer
)


class UserViewSet(ZhiyiAbstractModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    lookup_field = 'id'
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    lookup_field = 'id'

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


