# -*- coding: utf-8 -*-
# Author: YuZhiYi
# @Time : 2018/9/27 16:08
# @File : ZhiyiFilter.py
from rest_framework.filters import BaseFilterBackend
from django.db.models import Q
from rest_framework.compat import coreapi, coreschema
from django.utils.encoding import force_str

class GoodinfoPriceFilter(BaseFilterBackend):
    min_price_query_param = 'min_price'
    min_price_description = '最低价格'
    max_price_query_param = 'max_price'
    max_price_description = '最高价格'


    def filter_queryset(self, request, queryset, view):
        min_price = request.query_params.get(self.min_price_query_param, '')
        max_price = request.query_params.get(self.max_price_query_param,'')

        if min_price and max_price:
            return queryset.filter(Q(price__gte=min_price) & Q(price__lte=max_price))
        if min_price:
            return queryset.filter(price__gte=min_price)
        if max_price:
            return queryset.filter(price__lte=max_price)
        return queryset

    def get_schema_fields(self, view):
        assert coreapi is not None, 'coreapi must be installed to use `get_schema_fields()`'
        assert coreschema is not None, 'coreschema must be installed to use `get_schema_fields()`'
        fields = [
            coreapi.Field(
                name=self.min_price_query_param,
                required=False,
                location='query',
                schema=coreschema.Number(
                    title='min_price',
                    description=force_str(self.min_price_description)
                )
            )
        ]
        if self.max_price_query_param is not None:
            fields.append(
                coreapi.Field(
                    name=self.max_price_query_param,
                    required=False,
                    location='query',
                    schema=coreschema.Number(
                        title='max_price',
                        description=force_str(self.max_price_description)
                    )
                )
            )
        return fields
