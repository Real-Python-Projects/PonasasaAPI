from django.urls import path,include


from .views import *
#...
from rest_framework import routers
router = routers.DefaultRouter()
router.register('pharmacyowner', PharmacyOwnerProfileViewSet, basename='pharmacyowner')
router.register('pharmacist', PharmacistViewSet, basename='pharmacist')
router.register('customer', CustomerViewSet, basename='customer')
router.register('pharmacy', PharmacyViewSet, basename='pharmacy')
router.register('pharmacybranch', PharmacyBranchViewSet, basename='pharmacybranch')
router.register('product', ProductViewSet, basename='product')
router.register('productmedia', ProductMediaViewSet, basename='productmedia')
router.register('customerorder', CustomerOrderViewSet, basename='product')
router.register('activity', ActivityViewSet, basename='activity')
router.register('messages', MessageViewSet, basename='messages')
router.register('prescription',PrescriptionViewSet, basename='prescription')
router.register('report',ReportViewSet, basename='report')
router.register('advertisement',AdvertisementViewSet, basename='advertisement')
router.register('orderdeliverystatus', OrderDeliveryStatusViewSet, basename='orderdeliverystatus')
router.register('productstransaction', ProductTransactionViewSet, basename='productstransaction')
#...

urlpatterns = [
    #...
    path('api/', include(router.urls)),
]