#-*- coding: UTF-8 -*-
from django import forms
from .models import Member

#实现水平排列单选按钮
class HorizontalRadioRenderer(forms.RadioSelect.renderer):
    def render(self):
        return mark_safe(u'\n'.join([u'&nbsp;&nbsp;&nbsp;%\s ' % w for w in self]))

class MemberInfoForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),max_length=128,label=u'会员名字',required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),max_length=128,label=u'密码',required=True)
    age = forms.IntegerField(widget=forms.Input(attrs={'class':'form-control'}),required=True)
    sex = forms.CharField(widget=forms.RadioSelect(choices=((u'male',u'男性'),(u'female',u'女性')),attrs={'class':'radio-inline'},renderer=HorizontalRadioRenderer),label=u'性别')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),max_length=128,label=u'电话号码')