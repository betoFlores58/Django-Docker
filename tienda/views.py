from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tienda
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse, request
from django.contrib.auth.models import User
from django.db.models import Q

class TiendaListView(ListView):
    model = Tienda
    context_object_name = 'productos'
    template_name = 'tienda/shop.html'

