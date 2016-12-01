#-*- coding: UTF-8 -*-
from django import forms
from .models import Member
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.conf import settings


#实现水平排列单选按钮
class HorizontalRadioRenderer(forms.RadioSelect.renderer):
    def render(self):
        return mark_safe(u'\n '.join([u'&nbsp;&nbsp;&nbsp;%\s ' % w for w in self]))
    

class MemberInfoForm(forms.ModelForm):
    error_messages = {
        'username_starts':_("username can't contain a space"),
        'username_invalid':_("username can't contain @"),
        'username_admin':_("username can't start with 'admin'"),
        'duplicate_username': _('A user with that username already exists.'),
        'duplicate_email': _('A user with that email already exists.'),
        'password_mismatch': _('The two password fields didn\'t match.'),
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
        
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            get_user_model()._default_manager.get(username=username)
        except get_user_model().DoesNotExist:
            if username.startswith((' ','\t')):
                raise forms.ValidationError(
                    self.error_messages['username_starts'],
                    code = 'username_starts'
                )   
            elif username.startswith('admin'):
                raise forms.ValidationError(
                    self.error_messages['username_admin'],
                    code='username_admin',                
                )
            elif '@' in username:
                raise forms.ValidationError(
                    self.error_messages['username_invalid'],
                    code='username_invalid',
                )            
            return username
        
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )
    
    def clean_email(self):
    
        # Since User.email is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        email = self.cleaned_data['email']
        try:
            get_user_model()._default_manager.get(email=email)
        except get_user_model().DoesNotExist:
            return email
        raise forms.ValidationError(
            self.error_messages['duplicate_email'],
            code='duplicate_email',
        )    
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        
        return password2
    
    def save(self, commit=True,login_ip=False):
        user = super(MemberInfoForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = not settings.USERS_VERIFY_EMAIL
        if login_ip:
            user.login_ip = login_ip
        if commit:
            user.save()
        return user
    
class RegistrationForm(MemberInfoForm):
    error_css_class = 'has-error'
    required_css_class = 'required'
    
class LoginactionForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),max_length=128,label=u'会员名字',required=True)
    username = forms.CharField(
        required = True,
        label=u"用户名",
        error_messages={'required':'请输入用户名'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u"用户名",
            }   
        )   
    ) 
    
    password = forms.CharField(
        required=True,
        label=u"密码",
        error_messages={'required':u'请输入密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"密码",
            }   
            ),  
    )
    
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"用户名和密码为必填项")
        else:
            cleaned_data = super(LoginactionForm,self).clean()
