# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
import uuid

from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse
from django.contrib.auth.base_user import BaseUserManager


#Spliting users in model using custom user
class CustomUser(AbstractUser):
    user_type_choices=((1,"Pharmacy Owner"),(2," Phermacist"),(3,"Customer"))
    user_type=models.CharField(max_length=255,choices=user_type_choices,default=3)
    # objects = models.UserManager()
    # role = models.CharField("User Type", max_length=10, choices=USER_TYPE, default='Customer')


class PharmacyOwnerManager(BaseUserManager):
 
    def create_pharmacyowner(self, first_name, last_name, email, qualification, university, password=None):
        if email is None:
            raise TypeError('Users must have an email address.')
        pharmacyowner = PharmacyOwnerProfile(first_name=first_name, last_name=last_name, 
                          email=self.normalize_email(email),
                          qualification=qualification, university=university)
        pharmacyowner.set_password(password)
        pharmacyowner.save()
        return pharmacyowner
 
 
class PharmacistManager(BaseUserManager):
 
    def create_phamacist(self, first_name, last_name, email, designation, company, password=None):
        if email is None:
            raise TypeError('Users must have an email address.')
        pharmacist = PharmacistProfile(first_name=first_name, last_name=last_name, 
                            email=self.normalize_email(email),
                            designation=designation, company=company)
        pharmacist.set_password(password)
        pharmacist.save()
        return pharmacist

class CustomerManager(BaseUserManager):
 
    def create_customer(self, first_name, last_name, email, designation, company, password=None):
        if email is None:
            raise TypeError('Users must have an email address.')
        customer = CustomerProfile(first_name=first_name, last_name=last_name, 
                            email=self.normalize_email(email),
                            designation=designation, company=company)
        customer.set_password(password)
        customer.save()
        return customer

class PharmacyOwnerProfile(models.Model):
    id=models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser, blank=True, null=True, on_delete=models.SET_DEFAULT, default=None)
    mobileNo = models.CharField(max_length=40)
    cnic = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    shop_name = models.CharField(max_length=30)
    objects=models.Manager()

    def __str__(self):
        return self.user.username


class PharmacistProfile(models.Model):
    id=models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser, models.SET_DEFAULT, default=None)
    gender = models.CharField(max_length=255)
    profile_pic = models.FileField()
    address = models.TextField()
    country = models.CharField(max_length=255, default=None)
    province = models.CharField(max_length=255, default=None)
    district = models.CharField(max_length=255, default=None)
    city = models.CharField(max_length=255, default=None)
    zip_code = models.CharField(max_length=255, default=None)
    phone_number = models.CharField(max_length=255, default=None)
    education = models.CharField(max_length=255, default=None)
    workplace = models.CharField(max_length=255, default=None)
    objects=models.Manager()


    def __str__(self):
        return self.user.username

class CustomerProfile(models.Model):
    id=models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser, models.SET_DEFAULT, default=None)
    objects=models.Manager()


    def __str__(self):
        return self.user.username


# class UserManager(BaseUserManager):
 
#     def get_by_natural_key(self, email):
#         return self.get(email=email)
 
 


class PharmacyBranch(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    license_no=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    contact_no=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    added_on=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Pharmacy(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    location_address = models.CharField(max_length=255)
    country = models.CharField(max_length=255, default=None)
    province = models.CharField(max_length=255, default=None)
    district = models.CharField(max_length=255, default=None)
    city = models.CharField(max_length=255, default=None)
    zip_code = models.CharField(max_length=255, default=None)
    phone_number = models.CharField(max_length=255, default=None)
    license_no = models.CharField(max_length=255)
    license_operate = models.FileField()
    health_safety_code = models.CharField(max_length=255)
    health_safety_code_doc = models.FileField(max_length=255)
    about = models.TextField(max_length=150)
    website = models.CharField(max_length=255)
    contact_no=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    added_on=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    price=models.IntegerField()
    gross=models.IntegerField()
    size=models.CharField(max_length=255)
    strength=models.CharField(max_length=255)
    instock=models.IntegerField()
    reader_limit=models.CharField(max_length=255)
    expire_date=models.DateField()
    added_by_pharmacist=models.ForeignKey(PharmacistProfile,on_delete=models.CASCADE)
    mfg_date=models.DateField()
    description=models.CharField(max_length=255)
    attention=models.CharField(max_length=255)
    frequecy=models.CharField(max_length=255)
    composition=models.CharField(max_length=255)
    notes=models.CharField(max_length=255)
    added_on=models.DateTimeField(auto_now_add=True)
    edited_on=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class ProductMedia(models.Model):
    id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    media_type_choice=((1,"Image"),(2,"Video"))
    media_type=models.CharField(max_length=255)
    media_content=models.FileField()
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.IntegerField(default=1)

class ProductTransaction(models.Model):
    id=models.AutoField(primary_key=True)
    transaction_type_choices=((1,"BUY"),(2,"SELL"))
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    transaction_product_count=models.IntegerField(default=1)
    transaction_type=models.CharField(choices=transaction_type_choices,max_length=255)
    transaction_description=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)

class CustomerOrders(models.Model):
    id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    purchase_price=models.CharField(max_length=255)
    coupon_code=models.CharField(max_length=255)
    discount_amt=models.CharField(max_length=255)
    product_status=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)

class OrderDeliveryStatus(models.Model):
    id=models.AutoField(primary_key=True)
    order_id=models.ForeignKey(CustomerOrders,on_delete=models.CASCADE)
    status=models.CharField(max_length=255)
    status_message=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=255)
    item = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    delivered = models.IntegerField(default=1)
    quantity = models.IntegerField()
    total = models.IntegerField()
    costofdelivery = models.IntegerField()
    delivery_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

class Messages(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.CharField(max_length=255)
    reciever = models.CharField(max_length=255)
    subject = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return f'{self.sender} sending message to {self.reciever}'

class NotificationPharmacist(models.Model):
    id = models.AutoField(primary_key=True)
    pharmacist_id = models.ForeignKey(PharmacistProfile, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class NotificationCustomer(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Prescription(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.OneToOneField(Product,on_delete=models.DO_NOTHING)
    item = models.CharField(max_length=255)
    patient = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.IntegerField()
    patient_contact = models.CharField(max_length=255)
    presciber_name = models.CharField(max_length=255)
    presciber_contact = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

class Report(models.Model):
    id = models.AutoField(primary_key=True)
    pharmacy = models.OneToOneField(PharmacyBranch,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name

class Advertisement(models.Model):
    id = models.AutoField(primary_key=True)
    pharmacy = models.OneToOneField(PharmacyBranch,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name

class ProductQuestions(models.Model):
    id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    user_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    question=models.TextField()
    answer=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.IntegerField(default=1)

class ProductReviews(models.Model):
    id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    user_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    review_image=models.FileField()
    rating=models.CharField(default="5",max_length=255)
    review=models.TextField(default="")
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.IntegerField(default=1)



#Mpesa intergration

# Create your models here.
class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, blank=True)
    is_deleted = models.BooleanField(default=False, blank=True)

    class Meta:
        abstract = True


class PaymentTransaction(models.Model):
    phone_number = models.CharField(max_length=30)
    amount = models.DecimalField(('amount'), max_digits=6, decimal_places=2, default=0)
    isFinished = models.BooleanField(default=False)
    isSuccessFull = models.BooleanField(default=False)
    trans_id = models.CharField(max_length=30)
    order_id = models.CharField(max_length=200)
    checkoutRequestID = models.CharField(max_length=100)
    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.phone_number, self.amount)


class Wallet(BaseModel):
    phone_number = models.CharField(max_length=30)
    available_balance = models.DecimalField(('available_balance'), max_digits=6, decimal_places=2, default=0)
    actual_balance = models.DecimalField(('actual_balance'), max_digits=6, decimal_places=2, default=0)
    date_modified = models.DateTimeField(auto_now=True, null=True)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

    def __str__(self):
        return self.phone_number

@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            PharmacyOwnerProfile.objects.create(user=instance)
        if instance.user_type==2:
            PharmacistProfile.objects.create(user=instance)
        if instance.user_type==3:
            CustomerProfile.objects.create(user=instance)

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.pharmacyownerprofile.save()
    if instance.user_type==2:
        instance.phermacistprofile.save()
    if instance.user_type==3:
        instance.customerprofile.save()