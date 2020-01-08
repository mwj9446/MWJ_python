from django.contrib import admin
from booktest.models import BookInfo, HeroInfo

# Register your models here.

admin.site.register(BookInfo)
admin.site.register(HeroInfo)
admin.site.site_header = '啥玩意!!'
admin.site.site_title = '啥玩意??'
admin.site.index_title = '啥玩意啊啊'
