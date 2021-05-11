from django.views.generic import ListView, DetailView,TemplateView, FormView,CreateView,UpdateView, DeleteView
from .models import Modelo
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse, request

# Create your views here.
class HomeListView(ListView):
    model = Modelo
    template_name = 'home.html'
    context_object_name = 'Modelo'  

class CVListView(TemplateView):
    model = Modelo
    template_name = 'cv.html'
    context_object_name = 'Modelo'

class ITLView(TemplateView):
    model = Modelo
    template_name = 'itl.html'
    context_object_name = 'Modelo'

class cvCreateView(CreateView):
    model = Modelo
    template_name = "agregar.html"
    fields = '__all__'
    context_object_name = 'Modelo'
    success_url = reverse_lazy('home')

class cvUpdateView(LoginRequiredMixin,UpdateView):
    model = Modelo
    template_name = "editar.html"
    fields = '__all__'
    context_object_name = 'Modelo'
    success_url = reverse_lazy('home')

class cvDeleteView(LoginRequiredMixin,DeleteView):
    model = Modelo
    template_name = 'eliminar.html'
    context_object_name = 'Modelo'
    success_url = reverse_lazy('home')

#Registro para crear nuevo usuario
def registro(request):
    data = {
        'form': CustomUserCreationForm
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Usuario registrado correctamente")
            return redirect(to="home")
        data["form"]=formulario
    return render(request,'registration/registro.html',data)
