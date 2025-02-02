from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.urls import resolve


# Create your views here.

def index(request):
    route_url=reverse('user:index')
    print("reverse反向解析的url是：",route_url)
    result = resolve(route_url)
    print("resolve解析的结果是：",result)
    return HttpResponse("Hello, world. You're at the user app's index.")


def index2(request,year,month,day):  #for url list
    #for url list
    kwargs = {'year':year,'month':month,'day':day}
    # args_0=[year,month,day]
    route_url=reverse('user:list',kwargs=kwargs)
    print("reverse反向解析的url是：",route_url)
    result = resolve(route_url)
    print("resolve解析的结果是：",result)
    return HttpResponse("Hello, world. You're at the user app's index2.")