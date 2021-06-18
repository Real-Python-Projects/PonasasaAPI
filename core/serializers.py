from django.db.models import fields
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
        model = CustomUser
        fields = ('username', 'password')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    # def __str__(self):
    #     return self.user

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
 
    def validate(self, data):
        # The `validate` method is where we make sure that the current
        # instance of `LoginSerializer` has "valid". In the case of logging a
        # user in, this means validating that they've provided an email
        # and password and that this combination matches one of the users in
        # our database.
        email = data.get('email', None)
        password = data.get('password', None)
 
        # The `authenticate` method is provided by Django and handles checking
        # for a user that matches this email/password combination. Notice how
        # we pass `email` as the `username` value since in our User
        # model we set `USERNAME_FIELD` as `email`.
        user = authenticate(username=email, password=password)
 
        # If no user was found matching this email/password combination then
        # `authenticate` will return `None`. Raise an exception in this case.
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            userObj = PharmacyOwnerProfile.objects.get(email=user.email)
        except PharmacyOwnerProfile.DoesNotExist:
            userObj = None 
            
        try:
            userObj = PharmacistProfile.objects.get(email=user.email)
        except PharmacistProfile.DoesNotExist:
            userObj = None 

        try:
            if userObj is None:
                userObj = CustomerProfile.objects.get(email=user.email)
        except CustomerProfile.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )        
 
        # Django provides a flag on our `User` model called `is_active`. The
        # purpose of this flag is to tell us whether the user has been banned
        # or deactivated. This will almost never be the case, but
        # it is worth checking. Raise an exception in this case.
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )
 
        # The `validate` method should return a dictionary of validated data.
        # This is the data that is passed to the `create` and `update` methods
        # that we will see later on.
        return {
            'email': user.email,
            'token': user.token
        }

class PharmacyOwnerRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)
 
    class Meta:
        model = PharmacyOwnerProfile
        fields = '__all__'
 
    def create(self, validated_data):
        return PharmacyOwnerProfile.objects.create_student(**validated_data)
 
class PhamacistRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)
 
    class Meta:
        model = PharmacistProfile
        fields = '__all__'
 
    def create(self, validated_data):
        return PharmacistProfile.objects.create_employee(**validated_data)

class PharmacyRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)
 
    class Meta:
        model = PharmacyProfile
        fields = ['id','user','address','website','rating','service_provided','time_operation'
        ,'deliver_information','license_number','license_number_document','health_safety_code','health_safety_code_doc','about'
        ,'photos','patners','coments','token','password','debut']
 
    def create(self, validated_data):
        return PharmacyProfile.objects.create_employee(**validated_data)
    #First Tech


class PharmacistSerializer(serializers.ModelSerializer):

    user = UserSerializer(required=True)

    class Meta:
        model = PharmacistProfile
        fields = ['user','profile_pic','name','address','country','province','city','district','zip_code','phone_number','education','work_place']
        


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





class PharmacySerializer(serializers.ModelSerializer):

    user = UserSerializer(required=True)

    class Meta:
        model = PharmacyProfile
        fields = ('id','user','contact_number','address','website','rating','service_provided','time_operation','deliver_information','license_number','license_number_document','health_safety_code','health_safety_code_doc','about'
        ,'photos','patners','coments','debut')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(
            UserSerializer(), validated_data=user_data)
        seller, created = PharmacyProfile.objects.update_or_create(user=user,
                                                                  contact_number=validated_data.pop(
                                                                     'contact_number'),
                                                                     
                                                                 address=validated_data.pop(
                                                                    'address'),
                                                                 website=validated_data.pop(
                                                                     'website'),
                                                                 rating=validated_data.pop(
                                                                     'rating'),
                                                                service_provided=validated_data.pop(
                                                                    'service_provided'),
                                                                deliver_information=validated_data.pop(
                                                                     'deliver_information'),
                                                                license_number=validated_data.pop(
                                                                     'license_number'),
                                                                license_number_document=validated_data.pop(
                                                                     'license_number_document'),
                                                                health_safety_code=validated_data.pop(
                                                                     'health_safety_code'),
                                                                health_safety_code_doc=validated_data.pop(
                                                                     'health_safety_code_doc'),
                                                                about=validated_data.pop(
                                                                     'about'),
                                                                photos=validated_data.pop(
                                                                     'photos'),
                                                                patners=validated_data.pop(
                                                                     'patners'),
                                                                coments=validated_data.pop(
                                                                      'coments'),
                                                               

                                                                 )
        return seller








# class PharmacySerializer(serializers.ModelSerializer):

#     user = UserSerializer(required=True)

#     class Meta:
#         model = PharmacyProfile
#         # fields = ['id','user','address','website','service_provided','rating','time_operation'
#         # ,'deliver_information','license_number','license_number_document','health_safety_code','health_safety_code_doc','about'
#         # ,'photos','patners','coments','debut']
#         fields = ('user','address')

#     def create(self, validated_data):
#         user_data = validated_data.pop('user','address')
#         user = UserSerializer.create(
#             UserSerializer(), validated_data=user_data)
#         buyer, created = PharmacyProfile.objects.update_or_create(
#             user=user,
#                                                                  address=validated_data.pop(
#                                                                      'address'),
#                                                                 #  cnic=validated_data.pop(
#                                                                 #      'cnic'),
#                                                                 #  city=validated_data.pop(
#                                                                 #      'city'),
#                                                                 #  address=validated_data.pop(
#                                                                 #      'address'),
#                                                                 #  shop_name=validated_data.pop(
#                                                                 #      'shop_name'),

#         )
#         return buyer

    

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



class PharmacyPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model=PharmacyPhotos
        fields="__all__"



class PharmacyBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model=PharmacyBranch
        fields="__all__"


class ProductSerliazer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields= ['profile_image','name','code','unit','pack_size','strength','in_stock','reorder_limit','total_price','gross','description','attention','frequency','composition','notes']

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
        model= Advertisement
        fields="__all__"

class NotificationCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=NotificationCustomer
        fields="__all__"

class NotificationPharmacistSerializer(serializers.ModelSerializer):
    class Meta:
        model=NotificationPharmacist
        fields="__all__"
