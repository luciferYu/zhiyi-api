# -*- coding: utf-8 -*-
# FILENAME : @File : ZhiyiMiddleware.py
# FUNCTION : 
# Author: YuZhiYi
# @Time : 2018/9/28 13:34
import json
import time
import traceback
from django.http import JsonResponse
from django.utils import deprecation
from loguru import logger
from rest_framework import status


class AccessMiddleware(deprecation.MiddlewareMixin):
    def process_request(self, request):
        self.start_time = time.time()
        return None

    def process_response(self, request, response):
        use_time = time.time() - self.start_time
        remote_addr = request.META.get('X-Real-Ip', None)
        if remote_addr is None:
            remote_addr = request.META.get('REMOTE_ADDR', 'unknown')

        try:
            username = request.auth.payload['username']
        except Exception:
            username = 'anonymous'

        try:
            req_body = json.loads(request.body)
        except Exception:
            # print(traceback.format_exc())
            req_body = ''

        try:
            resp_header = response.items()
        except:
            resp_header = ''

        try:
            resp_body = json.loads(response.content)
        except Exception:
            resp_body = ''

        req_meta = request.META
        msg = '[access] |user: %s|remote_ip: %s|agent: %s|method: %s|protocol: %s|path: %s|req_params: %s|req_body: %s\
        |resp_code: %s|resp_header: %s|resp_body: %s|use_time: %3.5f' % (
            username
            , remote_addr
            , req_meta['HTTP_USER_AGENT']
            , req_meta['REQUEST_METHOD']
            , req_meta['SERVER_PROTOCOL']
            , req_meta['PATH_INFO']
            , request.GET.dict()
            , req_body
            , response.status_code
            , resp_header
            , resp_body
            , use_time
        )
        logger.debug(msg)
        return response

    def process_exception(self, request, exception):
        msg = '[access] 记录访问日志错误 '
        logger.error(msg)
        resp = {}
        resp['data'] = {}
        resp['message'] = '服务器内部错误，请联系管理员'
        resp['code'] = status.HTTP_500_INTERNAL_SERVER_ERROR
        resp['data']['pagedata'] = {}
        resp['status'] = 'failed'
        return JsonResponse(resp, safe=False)
