from django.contrib import admin
from django.urls import path,include

from rest_framework import permissions

from core.mpesaurls import mpesa_urls

from django.urls import path,include
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="Ponasasa API documentation")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("core.urls")),
    path('api-auth/', include('rest_framework.urls')),  # new

    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')), 
    path('mpesa/', include(mpesa_urls)),
    path('docs/', schema_view),
]






