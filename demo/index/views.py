from django.shortcuts import render
from django.http import HttpResponse
import os


# Create your views here.

def index(request):
    with open(r'template/index.html', 'rb') as f:
        data = f.read()
        print(data)
    return HttpResponse(data)
