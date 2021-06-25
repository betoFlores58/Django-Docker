from django.urls import path
from .views import HomeListView, TemplateView, CVListView, registro, ITLView, cvCreateView,cvUpdateView,cvDeleteView, ResetPasswordView,ResetPasswordForm,ExtraView
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views
from django.contrib.auth.views import PasswordResetView

urlpatterns=[
    path('', HomeListView.as_view(), name='home'),
    path('cv/',CVListView.as_view(),name='cv'),
    path('registro/',registro,name="registro"),
    path('extra/',ExtraView.as_view(),name="extra"),
    path('itl/',ITLView.as_view(),name="itl"),
    path('search_results/', views.search_results, name = 'search_results'),
    path('cv/Nuevo', cvCreateView.as_view(), name='nuevo'),
    path('<int:pk>/editar/', cvUpdateView.as_view(), name='editar'),
    path('delete/<int:pk>/', cvDeleteView.as_view(), name = 'eliminar'),
    path('change-password/',auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html',success_url = '/'),name='change_password'),
    path('reset_password/',PasswordResetView.as_view(template_name='registration/password_change_form.html'),name="reset_password"),
    path('reset_password_done/',auth_views.PasswordChangeDoneView.as_view(template_name='registration/change-done.html'),name="reset_password_done"),
]
