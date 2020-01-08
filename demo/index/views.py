import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


# Create your views here.
def index(request, city, year):
    # print(1)
    # with open(r'template/index.html', 'r', encoding='utf-8') as f:
    #     data = f.read()
    # data = data.replace('{%content%}', '%s : %s' % (city, year))
    context = {'content': '%s:%s' % (city, year),
               'adict': {'name': 'mwj', 'sex': 'man'},
               'alist': [1, 2, 3]
               }
    return render(request, 'index.html', context)


def index2(request):
    print(request.user)
    with open(r'template/index.html', 'r', encoding='utf-8') as f:
        data = f.read()
    city = request.GET.get('city', '默认值')
    year = request.GET.get('year')

    data = data.replace('{%content%}', '%s : %s' % (city, year))

    return HttpResponse(data.encode())


def index3(request):
    print(3)
    with open(r'template/index.html', 'r', encoding='utf-8') as f:
        data = f.read()
    city = request.META.get('HTTP_CITY')
    year = request.META.get('HTTP_YEAR')
    data = data.replace('{%content%}', '%s : %s' % (city, year))

    return HttpResponse(data.encode())


def index4(request):
    print(4)
    with open(r'template/index.html', 'r', encoding='utf-8') as f:
        data = f.read()
    city = request.POST.get('city')
    year = request.POST.get('year')
    print(request.POST)
    data = data.replace('{%content%}', '%s : %s' % (city, year))

    return HttpResponse(data.encode())


def index5(request):
    print(5)
    with open(r'template/index.html', 'r', encoding='utf-8') as f:
        data = f.read()
    req_data = request.body.decode()
    req_data = json.loads(req_data)
    city = req_data.get('city')
    year = req_data.get('year')

    data = data.replace('{%content%}', '%s : %s' % (city, year))

    return HttpResponse(data.encode())
