#-*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser)

# Create your models here.
class MemberManager(BaseUserManager):
    def create_user(self,email,username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError(u'邮箱必填')
    
        user = self.model(
            email = self.normalize_email(email),
            username = username
        )
    
        user.set_password(password)
        user.save(using=self._db)
    
        return user
    
    def create_superuser(self,email,username,password):
        user = self.create_user(
            email,
            password = password,
            username = username,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user     
    
class Member(AbstractBaseUser):
    SEX_TYPES = (
        ('male', '男'),
        ('female', '女'),
    )    
    
    username = models.CharField(u'会员名字',max_length=128,unique=True)
    password = models.CharField(u'密码',max_length=128,)
    age = models.IntegerField(u'年龄',default=0,blank=True)
    sex = models.CharField(u'性别',max_length=16,choices=SEX_TYPES,)
    email = models.EmailField(u'邮箱',max_length=255,unique=True)
    phone = models.CharField(u'电话号码',max_length=128)
    portrait = models.ImageField(upload_to="member_img/",blank=True,null=True)      #头像
    login_ip = models.GenericIPAddressField(null=True,)
    register_time = models.DateTimeField(u'注册时间',auto_now_add=True,null=True)
    last_login_time = models.DateTimeField(u'登录时间',auto_now=True, null=True)
    is_delete = models.BooleanField(default=False)   
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    access_token = models.CharField(max_length=100, blank=True)
    refresh_token = models.CharField(max_length=100, blank=True)
    expires_in = models.BigIntegerField(default=0)    
    
    objects = MemberManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email',)

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Member'
        
    def get_full_name(self):
        # The user is identified by their username address
        return self.username
    
    def get_short_name(self):
        # The user is identified by their username address
        return self.username    
        
    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    @property
    def is_staff(self):
        return self.is_admin    