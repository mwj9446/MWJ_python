def my_middleware(get):
    print('init')
    def middleware(request):
        print('1'*20)
        res=get(request)
        print('2'*20)
        return res
    return middleware