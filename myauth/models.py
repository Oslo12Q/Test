# _*_coding:utf-8_*_
 
from django.db import models
from django.contrib.auth.models import (BaseUserManager, 
					AbstractBaseUser,
					PermissionsMixin,
					UserManager)
from django.utils import timezone


class User(AbstractBaseUser, PermissionsMixin):
    '''继承 AbstractBaseUser 和 PermissionsMixin 可以重用认证必需的属性和方法，也可以完全重写'''
    username = models.CharField(u'User Name', max_length=30, unique=True)
    mobile = models.CharField(u'Mobile', max_length=11, blank=True)
    email = models.EmailField(u'Email address', blank=True)
    is_staff = models.BooleanField(u'staff status', default=False)
    is_active = models.BooleanField(u'active', default=True)

    date_joined = models.DateTimeField(u'date joined', default=timezone.now)  # 如果用 Django 自带的 UserManager（见下面代码） 则必须，否则可不用

    USERNAME_FIELD = 'username'  # 指定代表用户名的字段名
    REQUIRED_FIELDS = ['email']  # 如果用 Django 自带的 UserManager 时必须，因为其创建超级用户时必须有 email，即在syncdb 创建时要求填写
    objects = UserManager() # 用 Django 自带的 UserManager，如果定义的字段出入较大，当然需要自己实现

    def get_full_name(self):
        '''启用 Django 自带 Admin 时需实现，因为 Admin 显示用户名时需要'''
        return self.username

    def get_short_name(self):
        '''启用 Django 自带 Admin 时需实现，因为 Admin 显示用户名时需要'''
        return self.username
