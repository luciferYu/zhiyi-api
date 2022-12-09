from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (
    UserSerializer
    , GroupSerializer
    # , LoginSerializer
    , ZhiyiTokenObtainPairSerializer
)
from django.contrib.auth import authenticate
from loguru import logger


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    lookup_field = 'id'
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    lookup_field = 'id'

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


# class Login(APIView):
#     """
#     login system
#     """
#     def post(self, request, format=None):
#         resp_dict = {'code': status.HTTP_400_BAD_REQUEST, 'success': False, 'msg': '请求参数有误', 'data': {}}
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             username = serializer.validated_data.get('username')
#             password = serializer.validated_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 resp_dict['data'] = {'user': username}
#                 resp_dict['msg'] = '登陆成功'
#                 resp_dict['success'] = True
#                 resp_dict['code'] = status.HTTP_200_OK
#             else:
#                 resp_dict['msg'] = '登陆验证失败'
#         return Response(resp_dict, status.HTTP_200_OK)


class ZhiyiTokenObtainPairView(TokenObtainPairView):
    serializer_class = ZhiyiTokenObtainPairSerializer
