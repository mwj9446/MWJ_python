from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.urls import reverse


def index(request):
    return HttpResponse('hahahahhahaha！')


def login(request):
    return HttpResponse('登录' + str(request))


def center(request):
    url = reverse('hello')
    print(url)
    return redirect(url)
    # return HttpResponse('用户中心')
