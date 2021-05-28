from django.urls import path,include


from .views import *
#...
from rest_framework import routers
router = routers.DefaultRouter()
router.register('pharmacyowner', PharmacyOwnerViewSet, basename='pharmacyowner')
router.register('pharmacist', PharmacistViewSet, basename='pharmacist')
router.register('pharmacy', PharmacyViewSet, basename='pharmacy')
router.register('pharmacybranch', PharmacyBranchViewSet, basename='pharmacybranch')
router.register('product', ProductViewSet, basename='product')
router.register('activity', ActivityViewSet, basename='activity')
router.register('messages', MessageViewSet, basename='messages')
#...

urlpatterns = [
    #...
    path('api/', include(router.urls)),
]