from django.urls import path,include

from django.contrib import admin
from django.urls import path

from .views import *
#...
from rest_framework import routers

from django.urls import path,include
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title="Ponasasa API documentation")

from core.mpesaurls import mpesa_urls

router = routers.DefaultRouter()
# router.register('customersignup', CustomerRegistrationViewSet, basename='customersignup')
# router.register('userlogin', UserLoginViewSet, basename='userlogin')
router.register('users', UserViewSet, basename='users')
router.register('pharmacyowner', PharmacyOwnerProfileViewSet, basename='pharmacyowner')
router.register('pharmacist', PharmacistViewSet, basename='pharmacist')
router.register('pharmacy', PharmacyViewSet, basename='pharmacy')
router.register('pharmacyimages', PharmacyPhotosViewSet, basename='pharmacyimages')
# router.register('pharmacybranch', PharmacyBranchViewSet, basename='pharmacybranch')
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
    path('api/users/', PharmacyRegistrationViewSet.as_view()),
    path('api/users/login/', UserLoginViewSet.as_view()),
    path('api/', include(router.urls)),
    path('docs/', schema_view),
    path('mpesa/', include(mpesa_urls)),
   
   path('api/v1/', include('core.djoser')),

   path('api/pharmacybranch/', views.PharmacyBranch_list),
   path('api/pharmacybranch/<int:id>/', views.PharmacyBranch_detail),
]



