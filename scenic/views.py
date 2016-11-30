# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from .models import Scenic
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from django.db import connection

# Create your views here.
def index(request):
    
    top_scenic_list = Scenic.objects.all()[:10]

    print(top_scenic_list.query)
    return render(request, 'index.html',locals())

def get_scenic_list(request):
    after_range_num = 5
    before_range_num = 4
    try:
        page = request.GET.get('page')
        if page is None:
            page = int(page)
            
        if page<1:
            page = 1
    except ValueError:
        page =1
        
    
    sceniclist = Scenic.objects.all();
    paginator = Paginator(sceniclist,10)
    
    try:
        sceniclist = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
        sceniclist = paginator.page(1)
        
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+before_range_num]
    else:
        page_range = paginator.page_range[0:int(page)+before_range_num]
        
    return render(request,'scenic/allfilms.html',locals())