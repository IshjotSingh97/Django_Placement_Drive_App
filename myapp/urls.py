
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('server',views.server,name='server'),
    path('index',views.index,name='index'),
    path('userfeedbackform',views.userfeedbackform,name='userfeedbackform'),
    path('submituserfeedbackform',views.submituserfeedbackform,name='submituserfeedbackform'),
    path('search',views.search,name='search'),
    path('about',views.about,name='about'),
    path('addtofavourite/<int:uid>/<int:pid>',views.addtofavourite,name='addtofavourite'),
    path('getfavourite/<int:uid>/',views.getfavourite,name='getfavourite'),


]

