#-*- coding: UTF-8 -*-
from django.shortcuts import render
from forms import MemberInfoForm
from models import Member
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = MemberInfoForm(request.POST,request.FILES)
        if not form.is_valid():
            return render(request,'member/register.html',{'form':form})
        else:
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            age = form.cleaned_data.get('age')
            sex = form.cleaned_data.get('sex')
            email = form.cleaned_data.get('email')
            portrait = request.FILES['image']
            login_ip = get_client_ip(request)
            member = Member(moviename=moviename,movieaddress=movieaddress,downloadlink=downloadlink,
                          style=style,language=language,image=image,original=str(user.webuser.id))
            movie.save()
            messages.add_message(request,messages.SUCCESS,u'注册成功.')  
            
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
    