from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.urls import reverse


def response(request):
    res = HttpResponse(content='自定义响应', content_type='text/html; charset=utf8', status=200)
    res['name'] = 'zhangquandan'
    return res


def my_json_response(request):
    data = {'name': 'yueyunpeng', 'age': '33'}

    return JsonResponse(data)


def center(request):
    return redirect('/login/response/')


def set_cookie(request):
    count = request.COOKIES.get('count')
    if count:
        count = int(count)
        count += 1
    else:
        count = 1

    res = HttpResponse('set cookie')
    res.set_cookie('count', count, max_age=360)
    return res


def set_session(request):
    count = request.session.get('count')
    if count:
        count = int(count)
        count += 1
    else:
        request.session['count'] = '1'
    request.session.set_expiry(None)
    request.session['count']=count
    print(count)
    return HttpResponse('set session')
