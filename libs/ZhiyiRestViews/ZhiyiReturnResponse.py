from django.http import JsonResponse


def returnResponse(data={}, code=200, message='请求成功',status='ok', **kwargs):
    resp = {}
    resp['data'] = {}
    resp['message'] = message
    resp['code'] = code
    resp['data']['pagedata'] = data
    resp['status'] = status
    if kwargs:
        for k, v in kwargs.items():
            resp['data'][k] = v
    return JsonResponse(resp, safe=False)
