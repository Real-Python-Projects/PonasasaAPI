from django.conf.urls import url

from .views import CustomObtainAuthToken

urlpatterns = [
    url(r'^authenticate/', CustomObtainAuthToken.as_view()),
]
