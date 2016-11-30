from django.contrib import admin
from .models import Scenic
from django_markdown.admin import MarkdownModelAdmin

# Register your models here.
class ScenicComentAdmin(MarkdownModelAdmin):
    list_display = ('scenicname','scenicaddress','country','province','city','scenictype','create_date')
    #fields = []
    
admin.site.register(Scenic,ScenicComentAdmin)
