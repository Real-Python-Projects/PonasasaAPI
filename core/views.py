from django.shortcuts import render
from .serializers import *
from .models import PharmacyOwnerProfile, PharmacistProfile, PharmacyBranch, Product,Pharmacy
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import  IsAdminUser

from datetime import datetime, timedelta

from django.db.models import Sum
from rest_framework import viewsets, generics

# Create your views here.
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import get_object_or_404

class PharmacyOwnerViewSet(viewsets.ModelViewSet):
    permisssion_classes = (IsAdminUser,)
    serializer_class = PharmacyOwnerSerializer
    queryset = PharmacyOwnerProfile.objects.all()
    def get(self, format=None):

        seller = PhamacyOwnerProfile.objects.all()
        serializer = PharmacyOwnerSerializer(seller, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PharmacyOwnerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)


class PharmacistViewSet(viewsets.ModelViewSet):
    permisssion_classes = (IsAdminUser,)
    serializer_class = PharmacistSerializer
    queryset = PharmacistProfile.objects.all()
    def get(self, format=None):

        seller = PharmacistProfile.objects.all()
        serializer = UserSerializer(seller, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PharmacistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)

class PharmacyViewSet(viewsets.ViewSet):
    permission_classes = (IsAdminUser,)

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
    permission_classes = (IsAdminUser,)

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
    permission_classes = (IsAdminUser,)

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
    permission_classes = (IsAdminUser,)

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
    permission_classes = (IsAdminUser,)

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