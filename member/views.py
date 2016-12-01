#-*- coding: UTF-8 -*-
from django.shortcuts import render
from .forms import MemberInfoForm
from .models import Member
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from django.http import HttpResponse
from django.contrib import messages

from .forms import RegistrationForm


# Create your views here.
def login(request):
    pass
    
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST,request.FILES)
        if not form.is_valid():
            return render(request,'member/register.html',{'form':form})
        else:
            
            #username = form.cleaned_data.get('username')
            #password1 = form.cleaned_data.get('password1')
            #password2 = form.cleaned_data.get('password2')
            
            #password = form.clean_password2()
            
            #age = form.cleaned_data.get('age')
            #sex = form.cleaned_data.get('sex')
            #email = form.cleaned_data.get('email')
            #phone = form.cleaned_data.get('phone')
            ##portrait = request.FILES['image']
            #login_ip = get_client_ip(request)
            #member = Member(username=username,password=password,age=age,phone=phone,
                          #sex=sex,email=email,login_ip=login_ip)
            #member.save()
            
            login_ip = get_client_ip(request)
            
            member = form.save(login_ip=login_ip)
            
            messages.add_message(request,messages.SUCCESS,u'注册成功.')  
    else:
        form = RegistrationForm();
    return render(request,'member/register.html',{'form':form})
            
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
    