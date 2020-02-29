
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('server',views.server,name='server'),
    path('index',views.index,name='index'),
    path('userfeedbackform',views.userfeedbackform,name='userfeedbackform')

]
