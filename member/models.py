#-*- coding: UTF-8 -*-
from django.db import models

# Create your models here.
class Member(models.Model):
    SEX_TYPES = (
        ('male', '男'),
        ('female', '女'),
    )    
    
    username = models.CharField(u'会员名字',max_length=128,)
    password = models.CharField(u'密码',max_length=128,)
    age = models.IntegerField(u'年龄',default=0,blank=True)
    sex = models.CharField(u'性别',max_length=16,choices=SEX_TYPES,)
    email = models.EmailField(u'邮箱')
    phone = models.CharField(u'电话号码',max_length=128)
    portrait = models.ImageField(upload_to="member_img/",blank=True,null=True)      #头像
    login_ip = models.GenericIPAddressField(null=True,)
    register_time = models.DateTimeField(u'注册时间',auto_now_add=True,null=True)
    last_login_time = models.DateTimeField(u'登录时间',auto_now=True, null=True)

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Member'
        
    def __str__(self):
        return self.username