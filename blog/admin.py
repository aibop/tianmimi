from django.contrib import admin
from .models import Dynamic,Attention,Follower
from django_markdown.admin import MarkdownModelAdmin

# Register your models here.
class DynamicAdmin(MarkdownModelAdmin):
    list_display = ('user','title','dtype','action','dynamicer','addtime')
    
class AttentionAdmin(MarkdownModelAdmin):
    list_display = ('user','follow_user')
    
class FollowerAdmin(MarkdownModelAdmin):
    list_display = ('follow_user','user')
    
admin.site.register(Dynamic,DynamicAdmin)
admin.site.register(Attention,AttentionAdmin)
admin.site.register(Follower,FollowerAdmin)