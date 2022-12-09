# -*- coding: utf-8 -*-
# Author: YuZhiYi
# @Time : 2018/9/18 20:28
# @File : ZhiyiAbstractViewSet.py
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.renderers import JSONRenderer
from django_filters.rest_framework import DjangoFilterBackend
#from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework import mixins
from .ZhiyiReturnResponse import returnResponse
from .ZhiyiPagination import StandardResultsSetPagination
from django.http import Http404
from rest_framework_simplejwt.authentication import JWTAuthentication

class ZhiyiListModelMixin(mixins.ListModelMixin):
    """
        List a queryset.
        """

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            pageinfo = {"pagination": {"count": self.paginator.page.paginator.count,
                                       "pageCount": self.paginator.page.paginator.num_pages,
                                       "size": self.paginator.get_page_size(request),
                                       "index": self.paginator.page.number}}
            #return self.get_paginated_response(serializer.data)
            return returnResponse(data=serializer.data, message="查询成功", **pageinfo)

        serializer = self.get_serializer(queryset, many=True)
        #return returnResponse(serializer.data)
        returnResponse(data=serializer.data, message="查询成功")

class ZhiyiRetrieveModelMixin(mixins.RetrieveModelMixin):
    """
    Retrieve a model instance.
    """
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
        except Http404:
            return returnResponse(code=404, message='没有相关记录', status='fail', data=None)
        else:
            return returnResponse(data=serializer.data, code=200, message='查询成功')

class ZhiyiUpdateModelMixin(mixins.UpdateModelMixin):
    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}
        except Http404:
            return returnResponse(code=404, message='没有相关记录', status='fail')
        except Exception as e:
            return returnResponse(code=500, message=str(e), status='fail')

        return returnResponse(data=serializer.data, code=200, message='更新商品推荐成功')

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

class ZhiyiDestroyModelMixin(mixins.DestroyModelMixin):
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            return returnResponse(code=404, message='没有相关记录', status='fail', data=None)
        else:
            return returnResponse(data=None, code=204, message='删除商品推荐成功')

    def perform_destroy(self, instance):
        instance.delete()

class ZhiyiCreateModelMixin(mixins.CreateModelMixin):
    """
        Create a model instance.
        """

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return returnResponse(data=serializer.data, code=201, message='新建成功')

    def perform_create(self, serializer):
        serializer.save()

class ZhiyiAbstractModelViewSet(ZhiyiListModelMixin,
                              ZhiyiRetrieveModelMixin,
                              ZhiyiUpdateModelMixin,
                              ZhiyiDestroyModelMixin,
                              ZhiyiCreateModelMixin,
                              viewsets.GenericViewSet):
    """
    自定义的模型类视图集更新
    """
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    authentication_classes = (JWTAuthentication,)
    permission_classes = ()
    # permission_classes = (IsAuthenticated,)
    throttle_classes = (UserRateThrottle, AnonRateThrottle)
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    renderer_classes = (JSONRenderer,)
