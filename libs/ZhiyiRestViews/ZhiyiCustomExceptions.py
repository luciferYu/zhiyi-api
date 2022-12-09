from rest_framework.views import exception_handler
from rest_framework import status
from django.db import DatabaseError
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.exceptions import *
from pymysql.err import OperationalError
from .ZhiyiReturnResponse import returnResponse


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status'] = 'fail'
        response.data['code'] = response.status_code
        response.data['message'] = response.data['detail']  # 增加message这个key
        del response.data['detail']  # 删掉原来的detail
        response.status_code = 200

    return response


def my_custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        view = context['view']
        if isinstance(exc, (DatabaseError)):
            # print('[%s]: %s' % (view, exc))
            response = Response({'message': '数据库错误  ' + str(exc), 'code': 507, 'status': 'fail', 'data': None},
                                status=status.HTTP_507_INSUFFICIENT_STORAGE)
        elif isinstance(exc, OperationalError):
            # print('[%s]: %s' % (view, exc))
            response = Response({'message': '数据库错误  '+ str(exc), 'code': 507, 'status': 'fail', 'data': None},
                                status=status.HTTP_507_INSUFFICIENT_STORAGE)
        elif isinstance(exc, ParseError):
            response = Response({'message': '请求格式有误  ' + str(exc),'code': 400, 'status': 'fail', 'data': None},
                                status=status.HTTP_400_BAD_REQUEST)
        elif isinstance(exc, AuthenticationFailed):
            response = Response({'message': '身份验证失败  '+ str(exc),'code': 401, 'status': 'fail', 'data': None},
                                status=status.HTTP_401_UNAUTHORIZED)
        elif isinstance(exc, NotAuthenticated):
            response = Response({'message': '没有身份验证  '+ str(exc), 'code': 403, 'status': 'fail', 'data': None},
                                status=status.HTTP_403_FORBIDDEN)
        elif isinstance(exc, NotAuthenticated):
            response = Response({'message': '没有身份验证  '+ str(exc),'code': 403, 'status': 'fail', 'data': None},
                                status=status.HTTP_403_FORBIDDEN)
        elif isinstance(exc, PermissionDenied):
            response = Response({'message': '没有权限  ' + str(exc),'code': 403, 'status': 'fail', 'data': None},
                                status=status.HTTP_403_FORBIDDEN)
        elif isinstance(exc, NotFound):
            size = int(context['request'].query_params.get('page_size',10))
            index = int(context['request'].query_params.get('page',1))
            count = view.filter_queryset(view.get_queryset()).count()
            pagecount = count//size + 1 if count%size > 0 else count//size
            pageinfo = {"pagination": {"count": count,
                                       "pageCount":pagecount,
                                       "size": size,
                                       "index": index}}
            response = returnResponse(code=404, status='fail',message="页面不存在",**pageinfo)
        elif isinstance(exc, NotAcceptable):
            response = Response({'message': 'Not Acceptable' + str(exc),'code': 406, 'status': 'fail', 'data': None},
                                status=status.HTTP_406_NOT_ACCEPTABLE)
        elif isinstance(exc, Throttled):
            response = Response({'message': '访问限速，请稍后再试  '+ str(exc),'code': 429, 'status': 'fail', 'data': None},
                                status=status.HTTP_429_TOO_MANY_REQUESTS)
        elif isinstance(exc, ValidationError):
            response = Response({'message': '数据验证失败  '+ str(exc), 'code': 400, 'status': 'fail', 'data': None},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            response = Response({'message': '服务器内部错误  ' + str(exc), 'code': 500,'status':'fail','data':None},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return response
