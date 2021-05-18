from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cv.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
]
