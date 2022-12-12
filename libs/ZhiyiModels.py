# -*- coding: utf-8 -*-
# @Time    : 2022/12/8 15:11
# @Author  : YuZhiYi
# @Email   : 
# @Software : zhiyi-api

from django.db import models


class ZhiyiAbstractManager(models.Manager):
    def all(self):
        return super(models.Manager, self).all().filter(delete_flag=0)


class ZhiyiAbstractModel(models.Model):
    """
    抽象模型类
    """
    create_time = models.DateTimeField(help_text='创建时间', verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(help_text='修改时间', verbose_name='修改时间', auto_now=True)
    desc = models.CharField(max_length=255, blank=True, null=True, default='', help_text='描述')
    status = models.IntegerField(choices=((0, '禁用'), (1, '启用')), default=1, help_text='0表示禁用;1表示启用',
                                 verbose_name='0表示禁用;1表示启用')
    deleted = models.IntegerField(choices=((0, '未删除'), (1, '删除')), default=0, help_text='0表示正常;1表示逻辑删除',
                                  verbose_name='0表示正常;1表示逻辑删除')
    extend = models.TextField(default='{}', help_text='扩展字段', verbose_name='扩展字段')

    class Meta:
        abstract = True

    # objects = ZhiyiAbstractManager()
