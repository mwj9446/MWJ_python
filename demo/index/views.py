from django.shortcuts import render
from django.http import HttpResponse
import os


# Create your views here.

def index(request,*args):
    with open(r'template/index.html', 'rb') as f:
        data = f.read()
    print(args)
    for i in args:
        print(i)
    return HttpResponse(data)
