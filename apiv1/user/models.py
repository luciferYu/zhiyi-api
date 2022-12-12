# -*- coding: utf-8 -*-
# @Time    : 2022/12/9 9:51
# @Author  : YuZhiYi
# @Email   : 
# @Software : zhiyi-api
from django.db import models
from libs.ZhiyiModels import ZhiyiAbstractModel
from django.contrib.auth.models import User, Group, Permission
from mptt.models import MPTTModel, TreeManyToManyField, TreeForeignKey


class Menu(MPTTModel):
    name = models.CharField(max_length=64, unique=True, blank=False, help_text='菜单名')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, db_constraint=False, null=True, blank=True, related_name='children')
    create_time = models.DateTimeField(help_text='创建时间', verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(help_text='修改时间', verbose_name='修改时间', auto_now=True)
    desc = models.CharField(max_length=255, blank=True, null=True, help_text='描述')
    status = models.IntegerField(choices=((0, '禁用'), (1, '启用')), default=1, help_text='0表示禁用;1表示启用',
                                 verbose_name='0表示禁用;1表示启用')
    deleted = models.IntegerField(choices=((0, '未删除'), (1, '删除')), default=0, help_text='0表示正常;1表示逻辑删除',
                                  verbose_name='0表示正常;1表示逻辑删除')
    extend = models.TextField(default='', help_text='扩展字段', verbose_name='扩展字段')

    def __str__(self):
        return self.name
    # class MPTTMeta:
    #     order_insertion_by = ['menu_name']



# todo 权限角色相关
class Role(ZhiyiAbstractModel):
    """角色表"""
    role_name = models.CharField('role_name', max_length=64, blank=False, help_text='用户角色名')
    role_desc = models.CharField('role_desc', max_length=255, blank=True, null=True, help_text='用户角色名')
    users = models.ManyToManyField(User, db_constraint=False, blank=True, related_name='RoleUsers')
    groups = models.ManyToManyField(Group, db_constraint=False, blank=True,  related_name='RoleGroups')
    menus = TreeManyToManyField(Menu, db_constraint=False, blank=True, related_name='RoleMenus')
    permissions = models.ManyToManyField(Permission, db_constraint=False, blank=True, related_name='RolePermissions')

    class Meta:
        permissions = [
            # ("change_task_status", "Can change the status of tasks"),
            # ("close_task", "Can remove a task by setting its status as closed"),
        ]

    def __str__(self):
        return self.role_name


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

