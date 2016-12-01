#-*- coding: UTF-8 -*-
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django_markdown.admin import MarkdownModelAdmin

from .models import Member

# Register your models here.
#class MemberComentAdmin(MarkdownModelAdmin):
    #list_display = ('username','age','sex','email','phone','login_ip','register_time','last_login_time')
    ##fields = []
    
#admin.site.register(Member,MemberComentAdmin)

# 新增用户表单
class UserCreateForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='密码', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput,
    )
    

    class Meta:
        model = Member
        fields = ('username', 'email')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
    
# 修改用户表单
class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Member
        fields = ('username','email', 'password', 'age', 'sex', 'is_active', 'is_admin')        

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
    
# 注册用户
class MemberAdmin(BaseUserAdmin):

    form = UserChangeForm
    add_form = UserCreateForm

    list_display = ('username', 'age', 'sex', 'email', 'is_delete', 'is_admin', 'phone')
    search_fields = ('username', 'email')
    list_filter = ('is_admin',)
    readonly_fields = ('register_time', 'last_login_time')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'portrait')}),
        ('Personal info', {'fields': ('register_time', 'last_login_time',)}),
        (
            'Open token info',
            {
                'fields': ('access_token', 'refresh_token', 'expires_in')
            }
            ),
        ('Permissions', {'fields': ('is_delete', 'is_admin', 'is_active')}),
        ('Important dates', {'fields': ('last_login_time',)}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('username', 'email', 'password1', 'password2'),
            }
            ),
    )
    ordering = ('register_time',)
    filter_horizontal = ()


admin.site.register(Member, MemberAdmin)
#admin.site.unregister(Group)