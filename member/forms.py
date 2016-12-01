#-*- coding: UTF-8 -*-
from django import forms
from .models import Member
from django.utils.safestring import mark_safe

#实现水平排列单选按钮
class HorizontalRadioRenderer(forms.RadioSelect.renderer):
    def render(self):
        return mark_safe(u'\n '.join([u'&nbsp;&nbsp;&nbsp;%\s ' % w for w in self]))

class MemberInfoForm(forms.ModelForm):
    error_messages = {
        'username_starts':"username can't contain a space",
        'username_invalid':"username can't contain @",
        'username_admin':"username can't start with 'admin'",
        'duplicate_username': 'A user with that username already exists.',
        'duplicate_email': 'A user with that email already exists.',
        'password_mismatch': 'The two password fields didn\'t match.',
    }    
    
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),max_length=128,label=u'会员名字',required=True)
    age = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}),label=u'年龄',required=True)
    sex = forms.CharField(widget=forms.RadioSelect(choices=((u'male',u'男性'),(u'female',u'女性')),attrs={'class':'radio-inline'}),label=u'性别')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),max_length=128,label=u'电话号码')
    
    #password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),max_length=128,label=u'密码',required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),max_length=128,label=u'密码',required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),max_length=128,label=u'确认密码',required=True)
    
    #portrait = forms.ImageField(label=u'上传头像')    
    
    class Meta:
        model = Member
        fields = ['username','password1','password2','age','sex','email','phone'] 
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        
        return password2