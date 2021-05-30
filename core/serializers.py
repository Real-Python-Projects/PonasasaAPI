from rest_framework import serializers, status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='password',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    # def __str__(self):
    #     return self.user


class PharmacistSerializer(serializers.ModelSerializer):

    user = UserSerializer(required=True)

    class Meta:
        model = PharmacistProfile
        fields = ['id','user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(
            UserSerializer(), validated_data=user_data)
        buyer, created = PharmacistProfile.objects.update_or_create(
            user=user,
            # mobileNo=validated_data.pop('mobileNo'),
            # location=validated_data.pop('location'),
            # address=validated_data.pop('address'),

        )
        return buyer

class CustomerSerializer(serializers.ModelSerializer):

    user = UserSerializer(required=True)

    class Meta:
        model = CustomerProfile
        fields = ['id','user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(
            UserSerializer(), validated_data=user_data)
        buyer, created = CustomerProfile.objects.update_or_create(
            user=user,
            # mobileNo=validated_data.pop('mobileNo'),
            # location=validated_data.pop('location'),
            # address=validated_data.pop('address'),

        )
        return buyer

class PharmacyOwnerSerializer(serializers.HyperlinkedModelSerializer):

    user = UserSerializer(required=True)

    class Meta:
        model = PharmacyOwnerProfile
        fields = ('id','user', 'mobileNo', 'cnic',
                  'city', 'address', 'shop_name')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(
            UserSerializer(), validated_data=user_data)
        seller, created = PharmacyOwnerProfile.objects.update_or_create(user=user,
                                                                 mobileNo=validated_data.pop(
                                                                     'mobileNo'),
                                                                 cnic=validated_data.pop(
                                                                     'cnic'),
                                                                 city=validated_data.pop(
                                                                     'city'),
                                                                 address=validated_data.pop(
                                                                     'address'),
                                                                 shop_name=validated_data.pop(
                                                                     'shop_name'),
                                                                 )
        return seller

class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model=Pharmacy
        fields="__all__"


class PharmacyBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model=PharmacyBranch
        fields="__all__"

class ProductSerliazer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"

class ProductMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductMedia
        fields="__all__"

class CustomerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomerOrders
        fields="__all__"

class OrderDeliveryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderDeliveryStatus 
        fields="__all__"
       
class ProductTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductTransaction
        fields="__all__"

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Messages
        fields="__all__"


class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Prescription
        fields="__all__"

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model=Report
        fields="__all__"

class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model=Prescription
        fields="__all__"

