#-*- coding: UTF-8 -*-
from django.db import models
#from django.contrib.auth.models import User
from member.models import Member

# Create your models here.
class Dynamic(models.Model):
    DYNAMIC_TYPES = (
        ('MY','我自己的'),
        ('AT','我关注的人')
    )
    
    user = models.ForeignKey(Member,related_name='mydynamic')
    title = models.CharField(u'标题',max_length=128,)
    dtype = models.CharField(max_length=2,choices=DYNAMIC_TYPES,)
    link = models.URLField(u'动态链接')
    action = models.CharField(u'动态',max_length=128,)
    dynamicer = models.ForeignKey(Member,related_name='to_dynamicer')
    addtime = models.DateTimeField(auto_now=True,blank=True)
    
    class Meta:
        verbose_name = '动态'
        verbose_name_plural = '动态列表'

        
    def __str__(self):
        return self.title
    

class Attention(models.Model):
    user = models.ForeignKey(Member,related_name='be_attention')
    follow_user  = models.ForeignKey(Member,related_name='attentioner')
    
    class Meta:
        verbose_name = '关注列表'
        verbose_name_plural = '动态列表'
        unique_together = (("user","follow_user"))
    
class Follower(models.Model):
    follow_user = models.ForeignKey(Member,related_name='follower')
    user = models.ForeignKey(Member,related_name='by_follow')
    
    class Meta:
        verbose_name = '被关注列表'
        verbose_name_plural = '被关注列表'
        unique_together = (("follow_user","user"))

    
    