from django.urls import path,include

from django.contrib import admin
from django.urls import path

from .views import *
#...
from rest_framework import routers

from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view


router = routers.DefaultRouter()
# router.register('customersignup', CustomerRegistrationViewSet, basename='customersignup')
# router.register('userlogin', UserLoginViewSet, basename='userlogin')
router.register('pharmacyowner', PharmacyOwnerProfileViewSet, basename='pharmacyowner')
router.register('pharmacist', PharmacistViewSet, basename='pharmacist')
router.register('customer', CustomerViewSet, basename='customer')
router.register('pharmacy', PharmacyViewSet, basename='pharmacy')
router.register('pharmacybranch', PharmacyBranchViewSet, basename='pharmacybranch')
router.register('product', ProductViewSet, basename='product')
router.register('productmedia', ProductMediaViewSet, basename='productmedia')
router.register('customerorder', CustomerOrderViewSet, basename='customerorder')
router.register('activity', ActivityViewSet, basename='activity')
router.register('messages', MessageViewSet, basename='messages')
router.register('prescription',PrescriptionViewSet, basename='prescription')
router.register('report',ReportViewSet, basename='report')
router.register('advertisement',AdvertisementViewSet, basename='advertisement')
router.register('orderdeliverystatus', OrderDeliveryStatusViewSet, basename='orderdeliverystatus')
router.register('productstransaction', ProductTransactionViewSet, basename='productstransaction')
router.register('customernotification', NotificationCustomerViewSet, basename='customernotification')
router.register('pharmacistnotifications', NotificationPharmacistViewSet, basename='pharmacistnotifications')

urlpatterns = [
    # #...
    path('api/users/', CustomerRegistrationViewSet.as_view()),
    path('api/users/login/', UserLoginViewSet.as_view()),
    path('api/', include(router.urls)),
    path('docs/', include_docs_urls(title='Polls API')),
]


mpesa_urls = [
    path('submit/', SubmitView.as_view(), name='submit'),
    path('confirm/', ConfirmView.as_view(), name='confirm'),
    path('check-online/', CheckTransactionOnline.as_view(), name='confirm-online'),
    path('check-transaction/', CheckTransaction.as_view(), name='check_transaction'),
]
