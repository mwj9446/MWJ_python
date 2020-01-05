from django.shortcuts import render
from django.http import HttpResponse
import os


# Create your views here.

def index(request, city, year):
    with open(r'template/index.html', 'r') as f:
        data = f.read()
    data = data.replace('{%content%}', '%s : %s' % (city, year))

    return HttpResponse(data.encode())
