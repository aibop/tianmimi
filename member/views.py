#-*- coding: UTF-8 -*-
from django.shortcuts import render,redirect,render_to_response
from .forms import MemberInfoForm,LoginactionForm,RegistrationForm
from .models import Member
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from django.http import HttpResponse
from django.contrib import messages
from django.template.context import RequestContext


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = LoginactionForm()
        if not form.is_valid():
            #return render_to_response(request,'member/login.html',{'form':form})
            return render_to_response('member/login.html',RequestContext(request,{'form':form})) 
        else:
            username = request.POST.get('username','')
            password = request.POST.get('password','')
            user = auth.authenticate(username=username,password=password)
            if user is not None and user.is_active:
                auth.login(request,user)
                return redirect('index')
            else:
                return render_to_response('member/login.html',RequestContext(request,{'form':form,'password_is_wrong':True}))            
        
    else:
        form = LoginactionForm()
        return render(request,'member/login.html',{'form':form}) 
        
    
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
    