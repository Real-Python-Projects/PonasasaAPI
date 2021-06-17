from django.contrib import admin
from django.urls import path,include

from rest_framework import permissions
from rest_framework import permissions




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("core.urls")),
    # path('api-auth/', include('rest_framework.urls')),  # new

    # path('api/v1/', include('djoser.urls')),
    # path('api/v1/', include('djoser.urls.authtoken')), 

]











