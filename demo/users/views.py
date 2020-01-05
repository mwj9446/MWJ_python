from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    a = request.META
    print(a)
    return HttpResponse(a)