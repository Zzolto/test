from calendar import c
from django.contrib import admin

# Register your models here.


from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','title','shortDescription','fullDescription', 'newsType')
    list_display_links = ('id', 'title')
    search_fields = ('title','shortDescription')


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'color')
    list_display_links = ('id', 'title')

admin.site.register(News, NewsAdmin)
admin.site.register(Type, TypeAdmin)