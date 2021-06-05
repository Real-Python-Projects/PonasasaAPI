from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import  IsAdminUser

from datetime import datetime, timedelta

from django.db.models import Sum
from rest_framework import viewsets, generics

# Create your views here.
from rest_framework.permissions import IsAuthenticated,AllowAny

from .renderers import UserJSONRenderer

from rest_framework.generics import get_object_or_404
from .permissions import IsPharmacyOwrner, IsPharmacist, IsCustomer

# class PharmacyOwnerProfileViewSet(viewsets.ModelViewSet):
#     permisssion_classes = (IsAdminUser)
#     serializer_class = PharmacyOwnerSerializer
#     queryset = PharmacyOwnerProfile.objects.all()
    
#     def get(self, format=None):

#         seller = PharmacyOwnerProfile.objects.all()
#         serializer = PharmacyOwnerSerializer(seller, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = PharmacyOwnerSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=ValueError):
#             serializer.create(validated_data=request.data)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.error_messages,
#                         status=status.HTTP_400_BAD_REQUEST)

 
class CustomerRegistrationViewSet(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = CustomerRegistrationSerializer

    @classmethod
    def get_extra_actions(cls):
        return []
 
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
 
class UserLoginViewSet(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserLoginSerializer

    @classmethod
    def get_extra_actions(cls):
        return []

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PharmacistViewSet(viewsets.ModelViewSet):
    permission_classes = [IsPharmacyOwrner]
    serializer_class = PharmacistSerializer
    queryset = PharmacistProfile.objects.all()
   
   
    def get(self, request, format=None):
        seller = PharmacistProfile.objects.all()
        serializer = UserSerializer(seller, many=True)
        return Response(serializer.data)
        return Response({'response':'You must be authorised'})

    def post(self, request):
        serializer = PharmacistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.error_messages,
                            status=status.HTTP_400_BAD_REQUEST)
        return Response({'response':'You must be authorised'})

class CustomerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsPharmacyOwrner]
    serializer_class = CustomerSerializer
    queryset = CustomerProfile.objects.all()
    def get(self, format=None):

        seller = CustomerProfile.objects.all()
        serializer = UserSerializer(seller, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)
# class PharmacistViewSet(viewsets.ViewSet):
#     permission_classes = (IsAdminUser,)

#     def list(self,request):
#         Pharmacist=Pharmacist.objects.all()
#         serializer=PharmacistSerializer(Pharmacist,many=True,context={"request":request})
#         response_dict={"error":False,"message":"All Pharmacist List Data","data":serializer.data}
#         return Response(response_dict)

#     def post(self,request):
#         try:
#             serializer= PharmacistSerializer(data=request.data,context={"request":request})
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             dict_response={"error":False,"message":"Pharmacist Data Save Successfully"}
#         except:
#             dict_response={"error":True,"message":"Error During Saving Company Data"}
#         return Response(dict_response)
    
#     def retrieve(self, request, pk=None):
#         queryset = Pharmacist.objects.all()
#         Pharmacist = get_object_or_404(queryset, pk=pk)
#         serializer = PharmacistSerliazer(Pharmacist, context={"request": request})

#         serializer_data = serializer.data
#         # Accessing All the Medicine Details of Current Medicine ID ..... 
#         #pass

#         return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

#     def update(self,request,pk=None):
#         try:
#             queryset=Pharmacist.objects.all()
#             Pharmacist=get_object_or_404(queryset,pk=pk)
#             serializer=PharmacistSerializer(Pharmacist,data=request.data,context={"request":request})
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             dict_response={"error":False,"message":"Successfully Updated Pharmacist Data"}
#         except:
#             dict_response={"error":True,"message":"Error During Updating Pharmacist Data"}

#         return Response(dict_response)

class PharmacyOwnerProfileViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def list(self,request):
        pharmacyOwnerProfile=PharmacyOwnerProfile.objects.all()
        serializer=PharmacyOwnerSerializer(pharmacyOwnerProfile,many=True,context={"request":request})
        response_dict={"error":False,"message":"All PharmacyOwnerProfile List Data","data":serializer.data}
        return Response(response_dict)

    def post(self,request):
        try:
            serializer= PharmacyOwnerSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"PharmacyOwnerProfile Data Save Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving Company Data"}
        return Response(dict_response)
    
    def retrieve(self, request, pk=None):
        queryset = PharmacyOwnerSerializer.objects.all()
        PharmacyOwnerProfile = get_object_or_404(queryset, pk=pk)
        serializer = PharmacyOwnerSerializer(PharmacyOwnerProfile, context={"request": request})

        serializer_data = serializer.data
        # Accessing All the Medicine Details of Current Medicine ID ..... 
        #pass

        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def update(self,request,pk=None):
        try:
            queryset=PharmacyOwnerSerializer.objects.all()
            PharmacyOwnerProfile=get_object_or_404(queryset,pk=pk)
            serializer=PharmacyOwnerSerializer(PharmacyOwnerProfile,data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Successfully Updated PharmacyOwnerProfile Data"}
        except:
            dict_response={"error":True,"message":"Error During Updating PharmacyOwnerProfile Data"}

        return Response(dict_response)

class PharmacyViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, IsPharmacyOwrner,IsAdminUser,]

    def list(self,request):
        pharmacy=Pharmacy.objects.all()
        serializer=PharmacySerializer(pharmacy,many=True,context={"request":request})
        response_dict={"error":False,"message":"All Pharmacy List Data","data":serializer.data}
        return Response(response_dict)

    def post(self,request):
        try:
            serializer= PharmacySerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Pharmacy Data Save Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving Company Data"}
        return Response(dict_response)
    
    def retrieve(self, request, pk=None):
        queryset = Pharmacy.objects.all()
        pharmacy = get_object_or_404(queryset, pk=pk)
        serializer = PharmacySerliazer(pharmacy, context={"request": request})

        serializer_data = serializer.data
        # Accessing All the Medicine Details of Current Medicine ID ..... 
        #pass

        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def update(self,request,pk=None):
        try:
            queryset=Pharmacy.objects.all()
            pharmacy=get_object_or_404(queryset,pk=pk)
            serializer=PharmacySerializer(pharmacy,data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Successfully Updated Pharmacy Data"}
        except:
            dict_response={"error":True,"message":"Error During Updating Pharmacy Data"}

        return Response(dict_response)


class PharmacyBranchViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, IsPharmacyOwrner,IsAdminUser,]

    def list(self,request):
        pharmacybranch=PharmacyBranch.objects.all()
        serializer=PharmacyBranchSerializer(pharmacybranch,many=True,context={"request":request})
        response_dict={"error":False,"message":"All Pharmacy Branch List Data","data":serializer.data}
        return Response(response_dict)

    def post(self,request):
        try:
            serializer= PharmacySerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Pharmacy Branch Data Save Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving Pharmacy Branch Data"}
        return Response(dict_response)
    
    def retrieve(self, request, pk=None):
        queryset = PharmacyBranch.objects.all()
        pharmacybranch = get_object_or_404(queryset, pk=pk)
        serializer = PharmacyBranchSerializer(pharmacybranch, context={"request": request})

        serializer_data = serializer.data
        # Accessing All the Medicine Details of Current Medicine ID ..... 
        #pass

        return Response({"error": False, "message": "Single Pharmacy Data Fetch", "data": serializer_data})

    def update(self,request,pk=None):
        try:
            queryset=PharmacyBranch.objects.all()
            pharmacybranch=get_object_or_404(queryset,pk=pk)
            serializer=PharmacyBranchSerializer(pharmacy,data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Successfully Updated Pharmacy Branch Data"}
        except:
            dict_response={"error":True,"message":"Error During Updating Pharmacy Branch Data"}

        return Response(dict_response)

class ProductViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny,IsAdminUser,]

    def list(self,request):
        product = Product.objects.all()
        serializer=ProductSerliazer(product,many=True,context={"request":request})
        response_dict={"error":False,"message":"All Product List Data","data":serializer.data}
        return Response(response_dict)

    def post(self,request):
        try:
            serializer= ProductSerliazer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Product Data Save Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving Product Data"}
        return Response(dict_response)
    
    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerliazer(product, context={"request": request})

        serializer_data = serializer.data
        # Accessing All the Medicine Details of Current Medicine ID ..... 
        #pass

        return Response({"error": False, "message": "Single Product Data Fetch", "data": serializer_data})

    def update(self,request,pk=None):
        try:
            queryset=Product.objects.all()
            product=get_object_or_404(queryset,pk=pk)
            serializer=ProductSerliazer(product,data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Successfully Updated Product Data"}
        except:
            dict_response={"error":True,"message":"Error During Updating Product Data"}

        return Response(dict_response)

class MessageViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, IsPharmacyOwrner,IsPharmacist,IsCustomer,IsAdminUser]

    def list(self,request):
        message = Messages.objects.all()
        serializer=MessageSerializer(message,many=True,context={"request":request})
        response_dict={"error":False,"message":"All Message List Data","data":serializer.data}
        return Response(response_dict)

    def post(self,request):
        try:
            serializer= MessageSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Message Data Save Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving Message Data"}
        return Response(dict_response)
    
    def retrieve(self, request, pk=None):
        queryset = Messages.objects.all()
        message = get_object_or_404(queryset, pk=pk)
        serializer = MessageSerializer(message, context={"request": request})

        serializer_data = serializer.data
        # Accessing All the Medicine Details of Current Medicine ID ..... 
        #pass

        return Response({"error": False, "message": "Single Message Data Fetch", "data": serializer_data})

    def update(self,request,pk=None):
        try:
            queryset=Message.objects.all()
            message=get_object_or_404(queryset,pk=pk)
            serializer=MessageSerializer(message,data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Successfully Updated Message Data"}
        except:
            dict_response={"error":True,"message":"Error During Updating Message Data"}

        return Response(dict_response)

class ActivityViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, IsPharmacyOwrner,IsPharmacist,IsAdminUser,]

    def list(self,request):
        activity = Activity.objects.all()
        serializer=ActivitySerializer(activity,many=True,context={"request":request})
        response_dict={"error":False,"message":"All Activity List Data","data":serializer.data}
        return Response(response_dict)

    def post(self,request):
        try:
            serializer= ActivitySerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Activity Data Save Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving Activity Data"}
        return Response(dict_response)
    
    def retrieve(self, request, pk=None):
        queryset = Activity.objects.all()
        activity = get_object_or_404(queryset, pk=pk)
        serializer = ActivitySerializer(activity, context={"request": request})

        serializer_data = serializer.data
        # Accessing All the Medicine Details of Current Medicine ID ..... 
        #pass

        return Response({"error": False, "message": "Single Activity Data Fetch", "data": serializer_data})

    def update(self,request,pk=None):
        try:
            queryset=Activity.objects.all()
            activity=get_object_or_404(queryset,pk=pk)
            serializer=ActivitySerializer(activity,data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Successfully Updated Activity Data"}
        except:
            dict_response={"error":True,"message":"Error During Updating Activity Data"}

        return Response(dict_response)


class PrescriptionViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, IsPharmacyOwrner,IsCustomer,IsPharmacist,IsAdminUser,]

    def list(self,request):
        prescription = Prescription.objects.all()
        serializer=PrescriptionSerializer(prescription,many=True,context={"request":request})
        response_dict={"error":False,"message":"All Prescription List Data","data":serializer.data}
        return Response(response_dict)

    def post(self,request):
        try:
            serializer= PrescriptionSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Prescription Data Save Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving Prescription Data"}
        return Response(dict_response)
    
    def retrieve(self, request, pk=None):
        queryset = Prescription.objects.all()
        prescription = get_object_or_404(queryset, pk=pk)
        serializer = PrescriptionSerializer(prescription, context={"request": request})

        serializer_data = serializer.data
        # Accessing All the Medicine Details of Current Medicine ID ..... 
        #pass

        return Response({"error": False, "message": "Single Prescription Data Fetch", "data": serializer_data})

    def update(self,request,pk=None):
        try:
            queryset=Prescription.objects.all()
            prescription=get_object_or_404(queryset,pk=pk)
            serializer=PrescriptionSerializer(prescription,data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Successfully Updated Prescription Data"}
        except:
            dict_response={"error":True,"message":"Error During Updating Prescription Data"}

        return Response(dict_response)

class ReportViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, IsPharmacyOwrner,IsPharmacist,IsAdminUser]
    def list(self,request):
        report = Report.objects.all()
        serializer=ReportSerializer(report,many=True,context={"request":request})
        response_dict={"error":False,"message":"All Report List Data","data":serializer.data}
        return Response(response_dict)

    def post(self,request):
        try:
            serializer= ReportSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Report Data Save Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving Report Data"}
        return Response(dict_response)
    
    def retrieve(self, request, pk=None):
        queryset = Report.objects.all()
        report = get_object_or_404(queryset, pk=pk)
        serializer = ReportSerializer(report, context={"request": request})

        serializer_data = serializer.data
        # Accessing All the Medicine Details of Current Medicine ID ..... 
        #pass

        return Response({"error": False, "message": "Single Report Data Fetch", "data": serializer_data})

    def update(self,request,pk=None):
        try:
            queryset=Report.objects.all()
            Report=get_object_or_404(queryset,pk=pk)
            serializer=ReportSerializer(Report,data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Successfully Updated Report Data"}
        except:
            dict_response={"error":True,"message":"Error During Updating Report Data"}

        return Response(dict_response)
class AdvertisementViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, IsPharmacyOwrner,IsAdminUser,]
    def list(self,request):
        advertisement = Advertisement.objects.all()
        serializer=AdvertisementSerializer(advertisement,many=True,context={"request":request})
        response_dict={"error":False,"message":"All Advertisement List Data","data":serializer.data}
        return Response(response_dict)

    def post(self,request):
        try:
            serializer= AdvertisementSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Advertisement Data Save Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving Advertisement Data"}
        return Response(dict_response)
    
    def retrieve(self, request, pk=None):
        queryset = Advertisement.objects.all()
        advertisement = get_object_or_404(queryset, pk=pk)
        serializer = AdvertisementSerializer(advertisement, context={"request": request})

        serializer_data = serializer.data
        # Accessing All the Medicine Details of Current Medicine ID ..... 
        #pass

        return Response({"error": False, "message": "Single Advertisement Data Fetch", "data": serializer_data})

    def update(self,request,pk=None):
        try:
            queryset=Advertisement.objects.all()
            advertisement=get_object_or_404(queryset,pk=pk)
            serializer=AdvertisementSerializer(advertisement,data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Successfully Updated Advertisement Data"}
        except:
            dict_response={"error":True,"message":"Error During Updating Advertisement Data"}

        return Response(dict_response)
    
    
class ProductMediaViewSet(viewsets.ViewSet):
    permission_classes = (IsAdminUser,IsAdminUser,)

    def list(self,request):
        productMedia = ProductMedia.objects.all()
        serializer=ProductMediaSerializer(productMedia,many=True,context={"request":request})
        response_dict={"error":False,"message":"All ProductMedia List Data","data":serializer.data}
        return Response(response_dict)

    def post(self,request):
        try:
            serializer= ProductMediaSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"ProductMedia Data Save Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving ProductMedia Data"}
        return Response(dict_response)
    
    def retrieve(self, request, pk=None):
        queryset = ProductMedia.objects.all()
        productMedia = get_object_or_404(queryset, pk=pk)
        serializer = ProductMediaSerializer(productMedia, context={"request": request})

        serializer_data = serializer.data
        # Accessing All the Medicine Details of Current Medicine ID ..... 
        #pass

        return Response({"error": False, "message": "Single ProductMedia Data Fetch", "data": serializer_data})

    def update(self,request,pk=None):
        try:
            queryset=ProductMedia.objects.all()
            productMedia=get_object_or_404(queryset,pk=pk)
            serializer=ProductMediaSerializer(productMedia,data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Successfully Updated ProductMedia Data"}
        except:
            dict_response={"error":True,"message":"Error During Updating ProductMedia Data"}

        return Response(dict_response)
    
class CustomerOrderViewSet(viewsets.ViewSet):
    permission_classes = (IsAdminUser,IsAdminUser,)

    def list(self,request):
        customerOrder = CustomerOrders.objects.all()
        serializer=CustomerOrderSerializer(customerOrder,many=True,context={"request":request})
        response_dict={"error":False,"message":"All CustomerOrder List Data","data":serializer.data}
        return Response(response_dict)

    def post(self,request):
        try:
            serializer= CustomerOrderSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"CustomerOrder Data Save Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving CustomerOrder Data"}
        return Response(dict_response)
    
    def retrieve(self, request, pk=None):
        queryset = CustomerOrders.objects.all()
        customerOrder = get_object_or_404(queryset, pk=pk)
        serializer = CustomerOrderSerializer(customerOrder, context={"request": request})

        serializer_data = serializer.data
        # Accessing All the Medicine Details of Current Medicine ID ..... 
        #pass

        return Response({"error": False, "message": "Single CustomerOrder Data Fetch", "data": serializer_data})

    def update(self,request,pk=None):
        try:
            queryset=CustomerOrders.objects.all()
            customerOrder=get_object_or_404(queryset,pk=pk)
            serializer=CustomerOrderSerializer(customerOrder,data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Successfully Updated CustomerOrder Data"}
        except:
            dict_response={"error":True,"message":"Error During Updating CustomerOrder Data"}

        return Response(dict_response)
    
class ProductTransactionViewSet(viewsets.ViewSet):
    permission_classes = (IsAdminUser,IsAdminUser,)

    def list(self,request):
        productTransaction = ProductTransaction.objects.all()
        serializer=ProductTransactionSerializer(productTransaction,many=True,context={"request":request})
        response_dict={"error":False,"message":"All ProductTransaction List Data","data":serializer.data}
        return Response(response_dict)

    def post(self,request):
        try:
            serializer= ProductTransactionSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"ProductTransaction Data Save Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving ProductTransaction Data"}
        return Response(dict_response)
    
    def retrieve(self, request, pk=None):
        queryset = ProductTransaction.objects.all()
        productTransaction = get_object_or_404(queryset, pk=pk)
        serializer = ProductTransactionSerializer(productTransaction, context={"request": request})

        serializer_data = serializer.data
        # Accessing All the Medicine Details of Current Medicine ID ..... 
        #pass

        return Response({"error": False, "message": "Single ProductTransaction Data Fetch", "data": serializer_data})

    def update(self,request,pk=None):
        try:
            queryset=ProductTransaction.objects.all()
            productTransaction=get_object_or_404(queryset,pk=pk)
            serializer=ProductTransactionSerializer(productTransaction,data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Successfully Updated ProductTransaction Data"}
        except:
            dict_response={"error":True,"message":"Error During Updating ProductTransaction Data"}

        return Response(dict_response)
    
class OrderDeliveryStatusViewSet(viewsets.ViewSet):
    permission_classes = (IsAdminUser,IsAdminUser,)

    def list(self,request):
        orderDeliveryStatus = OrderDeliveryStatus.objects.all()
        serializer=OrderDeliveryStatusSerializer(orderDeliveryStatus,many=True,context={"request":request})
        response_dict={"error":False,"message":"All OrderDeliveryStatus List Data","data":serializer.data}
        return Response(response_dict)

    def post(self,request):
        try:
            serializer= OrderDeliveryStatusSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"OrderDeliveryStatus Data Save Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving OrderDeliveryStatus Data"}
        return Response(dict_response)
    
    def retrieve(self, request, pk=None):
        queryset = OrderDeliveryStatus.objects.all()
        orderDeliveryStatus = get_object_or_404(queryset, pk=pk)
        serializer = OrderDeliveryStatusSerializer(orderDeliveryStatus, context={"request": request})

        serializer_data = serializer.data
        # Accessing All the Medicine Details of Current Medicine ID ..... 
        #pass

        return Response({"error": False, "message": "Single OrderDeliveryStatus Data Fetch", "data": serializer_data})

    def update(self,request,pk=None):
        try:
            queryset=OrderDeliveryStatus.objects.all()
            orderDeliveryStatus=get_object_or_404(queryset,pk=pk)
            serializer=OrderDeliveryStatusSerializer(orderDeliveryStatus,data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Successfully Updated OrderDeliveryStatus Data"}
        except:
            dict_response={"error":True,"message":"Error During Updating OrderDeliveryStatus Data"}

        return Response(dict_response)


class NotificationCustomerViewSet(viewsets.ViewSet):
    permission_classes = (IsAdminUser,IsAdminUser,)

    def list(self,request):
        notificationCustomer = NotificationCustomer.objects.all()
        serializer=NotificationCustomerSerializer(notificationCustomer,many=True,context={"request":request})
        response_dict={"error":False,"message":"All NotificationCustomer List Data","data":serializer.data}
        return Response(response_dict)

    def post(self,request):
        try:
            serializer= NotificationCustomerSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"NotificationCustomer Data Save Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving NotificationCustomer Data"}
        return Response(dict_response)
    
    def retrieve(self, request, pk=None):
        queryset = NotificationCustomer.objects.all()
        notificationCustomer = get_object_or_404(queryset, pk=pk)
        serializer = NotificationCustomerSerializer(notificationCustomer, context={"request": request})

        serializer_data = serializer.data
        # Accessing All the Medicine Details of Current Medicine ID ..... 
        #pass

        return Response({"error": False, "message": "Single NotificationCustomer Data Fetch", "data": serializer_data})

    def update(self,request,pk=None):
        try:
            queryset=NotificationCustomer.objects.all()
            notificationCustomer=get_object_or_404(queryset,pk=pk)
            serializer=NotificationCustomerSerializer(notificationCustomer,data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Successfully Updated NotificationCustomer Data"}
        except:
            dict_response={"error":True,"message":"Error During Updating NotificationCustomer Data"}

        return Response(dict_response)

class NotificationPharmacistViewSet(viewsets.ViewSet):
    permission_classes = (IsAdminUser,IsAdminUser,)

    def list(self,request):
        notificationPharmacist = NotificationPharmacist.objects.all()
        serializer=NotificationPharmacistSerializer(notificationPharmacist,many=True,context={"request":request})
        response_dict={"error":False,"message":"All NotificationPharmacist List Data","data":serializer.data}
        return Response(response_dict)

    def post(self,request):
        try:
            serializer= NotificationPharmacistSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"NotificationPharmacist Data Save Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving NotificationPharmacist Data"}
        return Response(dict_response)
    
    def retrieve(self, request, pk=None):
        queryset = NotificationPharmacist.objects.all()
        notificationPharmacist = get_object_or_404(queryset, pk=pk)
        serializer = NotificationPharmacistSerializer(notificationPharmacist, context={"request": request})

        serializer_data = serializer.data
        # Accessing All the Medicine Details of Current Medicine ID ..... 
        #pass

        return Response({"error": False, "message": "Single NotificationPharmacist Data Fetch", "data": serializer_data})

    def update(self,request,pk=None):
        try:
            queryset=NotificationPharmacist.objects.all()
            notificationPharmacist=get_object_or_404(queryset,pk=pk)
            serializer=NotificationPharmacistSerializer(notificationPharmacist,data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Successfully Updated NotificationPharmacist Data"}
        except:
            dict_response={"error":True,"message":"Error During Updating NotificationPharmacist Data"}

        return Response(dict_response)