from django.urls import path, include
from .views import *
from rest_framework import routers



routers =  routers.SimpleRouter()
routers.register(r'news', NewsViewSet)
routers.register(r'type', NewsTypeViewSet)


urlpatterns = [
    path('', index, name = 'home'),
    path('v1/', include(routers.urls)),
 ]