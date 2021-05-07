from django.urls import path
from .views import HomeListView, TemplateView, CVListView, registro
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns=[
    path('', HomeListView.as_view(), name='home'),
    path('cv/',CVListView.as_view(),name='cv'),
    path('registro/',registro,name="registro"),
]
