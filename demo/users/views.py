from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
def decorator(fn):
    def inner(request,*args,**kwargs):
        print('ok1')
        return fn(request,*args,**kwargs)
    return inner

class ClassView(View):
    def get(self,request):
        return HttpResponse('get')
    def post(self,request):
        return HttpResponse('post')

