# -*- coding: utf-8 -*-
# @Time    : 2022/12/9 10:26
# @Author  : YuZhiYi
# @Email   : 
# @Software : zhiyi-api
# todo 审计相关
from libs.ZhiyiModels import ZhiyiAbstractModel
from django.db import models


class OperateLog(ZhiyiAbstractModel):
    """操作日志表"""
    user_id = models.IntegerField('user id', blank=False, null=False, help_text='用户id')
    username = models.CharField('username', max_length=64, blank=False, null=False, help_text='用户名')
    nickname = models.CharField('nickname', max_length=64, blank=False, null=False, help_text='用户姓名')
    remote_ip = models.GenericIPAddressField('remote_ip', max_length=32, blank=False, help_text='访问ip')
    request_params = models.TextField('request_params', blank=False, help_text='请求参数')
    content = models.TextField('content', blank=False, help_text='操作内容')
    origin_data = models.TextField('origin_data', blank=False, help_text='更新前的内容')
    modify_data = models.TextField('origin_data', blank=False, help_text='更新后的内容')

