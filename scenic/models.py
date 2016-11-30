#-*- coding: UTF-8 -*-
from django.db import models
import markdown

# Create your models here.
class Scenic(models.Model):
    culturalRelics = 'CR'
    classicalGarden = 'CG'
    literatureArt = 'LA'
    religiousCulture = 'RC'
    ruralLandscape = 'RL'
    modernFacilities = 'MF'
    folkCustom = 'FC'
    eatingShopping = 'ES'
    
    SCENIC_TYPES = (
        (culturalRelics, '文物古迹'),
        (classicalGarden, '古典园林'),
        (literatureArt, '文学艺术'),
        (religiousCulture, '宗教文化'),
        (ruralLandscape, '城乡风貌'),
        (modernFacilities, '现代设施'),
        (folkCustom, '民俗风情'),
        (eatingShopping, '饮食与购物类'),
    )    
    
    scenicname = models.CharField(u'名称',max_length=255,)
    scenicaddress = models.CharField(u'地址',max_length=200,)
    country = models.CharField(u'国家',max_length=128,)
    province = models.CharField(u'省',max_length=128,)
    city = models.CharField(u'市',max_length=128,)
    scenictype = models.CharField(max_length=2,choices=SCENIC_TYPES,)
    intro = models.TextField(u'简介',blank=True)
    cover = models.ImageField(upload_to="cover/",blank=True,null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Scenic'
        verbose_name_plural = 'Scenics'
        
    def __str__(self):
        return self.scenicname    
    
    def get_intro_as_markdown(self):
        return markdown.markdown(self.intro,safe_model='escape')
    
    def get_intro_preview(self):
        if len(self.intro) > 255:
            return u'{0}...'.format(self.intro[:255])
        else:
            return self.intro
    
    def get_intro_preview_as_markdown(self):
        return markdown.markdown(self.get_intro_preview(), safe_mode = 'escape')

    def create_tags(self, tags):
        tags = tags.strip()
        tag_list = tags.split(' ')
        for tag in tag_list:
            t, created = Tag.objects.get_or_create(tag=tag.lower(), scenic = self)

    def get_tags(self):
        return Tag.objects.filter(scenic = self)  
    
    def get_pictures(self):
        return Picture.object.filter(scenic = self)
        

    
class Tag(models.Model):
    tag = models.CharField(max_length=64)
    scenic = models.ForeignKey(Scenic)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        unique_together = (('tag', 'scenic'),)
        index_together = [['tag', 'scenic'],]

    def __str__(self):          #python 2 __unicode__ 
        return self.tag
    
class Picture(models.Model):
    picture = models.ImageField(upload_to="picture/",blank=True,null=True)
    scenic = models.ForeignKey(Scenic, related_name='scenic_pic',)
    
    class Meta:
        verbose_name = 'Picture'
        verbose_name_plural = 'Picture'
        
    def __str__(self):
        return self.picture
    