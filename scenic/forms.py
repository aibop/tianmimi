#-*- coding: UTF-8 -*-
from django import forms
from .models import Scenic

class HorizontalCheckRenderer(forms.CheckboxSelectMultiple.renderer):
    def render(self):
        return mark_safe(u'\n'.join([u'&nbsp;&nbsp;&nbsp;%s\n ' % w for w in self]))

class ScenicInfoForm(forms.ModelForm):
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
    
    scenicname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),max_length=255,label=u'景点名',required=True)
    scenicaddress = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label=u'具体地址',max_length=200)
    country = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label=u'国家',max_length=128)
    province = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label=u'省',max_length=128)
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label=u'市',max_length=128)
    scenictype = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(renderer=HorizontalCheckRenderer),
                                      choices=SCENIC_TYPES,required=False,label=u'类型')
    intro = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}),label=u'简介',required=False)
    
    class Meta:
        model = Scenic
        fields = ['scenicname','scenicaddress','country','province','city','scenictype','intro']