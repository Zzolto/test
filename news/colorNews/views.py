from gettext import install
from django.shortcuts import render
from .models import *
from rest_framework import generics, viewsets
from .serializers import *
from rest_framework.views import *
from rest_framework.response import Response
from django.forms import model_to_dict
# Create your views here.


class NewsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsTypeAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeNewsSerializers


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsTypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeNewsSerializers



    

def index(request):
    news = News.objects.all()
    types = Type.objects.all()
    context = {
        'news':news,
        'title':'Список новостей',
        'types':types
    }
    # for i in news:
    #     news_type.append('news_title':news.title, newsShortDesc')
    return render(request,'news/index.html', context)

def get_type(request, type_id):
    types = Type.objects.all()
    news = News.objects.filter(newsType_id = type_id)
    type = Type.objects.get(pk = type_id)
    return render(request,'news/type.html', {'news':news,'types':types, 'type':type})


def get_color(request, type_id):
    types = Type.objects.all()
    news = News.objects.filter(newsType_id = type_id)
    type = Type.objects.get(pk = type_id)
    return render(request,'news/type.html', {'news':news,'types':types, 'type':type})


