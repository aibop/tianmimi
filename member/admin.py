from django.contrib import admin
from .models import Member
from django_markdown.admin import MarkdownModelAdmin

# Register your models here.
class MemberComentAdmin(MarkdownModelAdmin):
    list_display = ('username','age','sex','email','phone','login_ip','register_time','last_login_time')
    #fields = []
    
admin.site.register(Member,MemberComentAdmin)