# -*- coding: utf-8 -*-
# @Time    : 2022/12/9 9:51
# @Author  : YuZhiYi
# @Email   : 
# @Software : zhiyi-api
from django.contrib.auth.models import User, Group
from libs.ZhiyiModels import ZhiyiAbstractModel

# todo 权限角色相关
# class AuthRole(models.Model):
#     """角色表"""
#     # e.g: add_user
#     role_id = models.CharField('role id', max_length=64, blank=False, unique=True, help_text='用户角色标识')
#     # e.g 添加用户
#     role_name = models.CharField('role name', max_length=64, blank=False, help_text='用户角色名')
#
#     class Meta:
#         db_table = 'auth_role'
#
#     def __str__(self):
#         return self.role_name
#
#
# class AuthUserRole(models.Model):
#     """用户角色关系表"""
#     user_id = models.IntegerField('user id', blank=False, help_text='用户id', unique=True)
#     role_ids = models.CharField('role ids', blank=True, default=None, max_length=256, help_text='用户的角色ids')
#
#     class Meta:
#         db_table = 'auth_user_roles'
#
#
# class AuthRolePms(models.Model):
#     """角色权限关系表"""
#     role_id = models.CharField('role id', max_length=64, blank=False, help_text='用户角色标识')
#     pms_code = models.CharField('permission code', blank=False, max_length=64, help_text='权限code')
#
#     class Meta:
#         db_table = 'auth_role_pms'
#         unique_together = ('role_id', 'pms_code')
#
#
# class AuthGroup(models.Model):
#     """用户小组"""
#     name = models.CharField('group name', max_length=32, blank=False, null=False, help_text='分组名')
#     comment = models.CharField('comment', max_length=32, blank=True, help_text='备注')
#
#     class Meta:
#         db_table = 'auth_group'
#
#     def __str__(self):
#         return self.name
#
#
# class AuthUserGroups(models.Model):
#     """用户分组关系"""
#     IS_ADMIN_CHOICES = (
#         (0, '否'),
#         (1, '是'),
#     )
#
#     user_id = models.IntegerField('user id', blank=False, null=False, help_text='用户ID')
#     group_id = models.IntegerField('group id', blank=False, null=False, help_text='分组ID')
#     is_admin = models.SmallIntegerField('is admin', blank=False, choices=IS_ADMIN_CHOICES, default=0,
#                                         help_text='是否是组管理员')
#
#     class Meta:
#         db_table = 'auth_cusergroups'
#         unique_together = ('user_id', 'group_id')
