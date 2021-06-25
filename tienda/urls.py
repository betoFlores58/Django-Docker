from django.conf.urls import url
from .views import TiendaListView
from django.shortcuts import render
from django.urls import path

urlpatterns=[
    path('',TiendaListView.as_view(),name='shop'),
]