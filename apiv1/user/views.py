from loguru import logger
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, status
from libs.ZhiyiRestViews.ZhiyiAbstractViewSet import ZhiyiAbstractModelViewSet
from .serializers import (
    UserSerializer
    , GroupSerializer
)


class UserViewSet(ZhiyiAbstractModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.

    GET: /apiv1/user/?username=test&ordering=-id&page=1&page_size=5&username=yuzhiyi&fields=id,username

    """
    lookup_field = 'id'
    filterset_fields = ('username',)  # 过滤字段
    search_fields = ('username',)  # 搜索字段
    ordering = ('id', 'username')  # 排序字段
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


