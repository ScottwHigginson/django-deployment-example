from django.contrib import admin
from django.urls import path, re_path, include
from basic_app import views

#template tagging
app_name = 'basic_app'


urlpatterns = [

     re_path(r'^$',views.index, name='index'),
     re_path(r'^other/$',views.other, name='other'),
     re_path(r'^relative/$',views.relative, name='relative'),

]
