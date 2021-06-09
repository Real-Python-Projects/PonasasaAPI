from django.contrib import admin
from django.urls import path,include

from rest_framework import permissions

from core.mpesaurls import mpesa_urls

from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("core.urls")),
    path('api-auth/', include('rest_framework.urls')),  # new

    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')), 
    path('mpesa/', include(mpesa_urls)),
]





