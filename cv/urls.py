from django.urls import path
from .views import HomeListView, TemplateView, CVListView, registro, ITLView, cvCreateView,cvUpdateView,cvDeleteView
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns=[
    path('', HomeListView.as_view(), name='home'),
    path('cv/',CVListView.as_view(),name='cv'),
    path('registro/',registro,name="registro"),
    path('itl/',ITLView.as_view(),name="itl"),
    path('cv/Nuevo', cvCreateView.as_view(), name='nuevo'),
    path('<int:pk>/editar', cvUpdateView.as_view(), name='editar'),
    path('delete/<int:pk>/', cvDeleteView.as_view(), name = 'eliminar'),
]
