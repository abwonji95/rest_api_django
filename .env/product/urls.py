from collections import namedtuple
from django.urls import path,include
from  . import views
from .views import *
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[

#product_list
    path('product_list/',views.product_list,name='list'),
    path('product_detail/<int:pk>/',views.product_detail,name='details'),
]