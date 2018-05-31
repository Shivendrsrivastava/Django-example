from django.conf.urls import url , include
from django.contrib import admin
from simple_app import views

# TEMPLATE_TAGGING
app_name = 'simple_app'


urlpatterns = [
    url(r'^relative' , views.relative , name = 'realtive'),
    url(r'^other' , views.other , name = 'other'),
    url(r'^index' , views.index , name = 'index'),

]
