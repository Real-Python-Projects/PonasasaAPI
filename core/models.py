from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class PharmacyOwnerProfile(models.Model):
    id=models.AutoField(primary_key=True)
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.SET_DEFAULT, default=None)
    mobileNo = models.CharField(max_length=40, default=None)
    cnic = models.CharField(max_length=30, default=None)
    city = models.CharField(max_length=30, default=None)
    address = models.CharField(max_length=30, default=None)
    shop_name = models.CharField(max_length=30, default=None)
    objects=models.Manager()

    def __str__(self):
        return self.user.username


class PharmacistProfile(models.Model):
    id=models.AutoField(primary_key=True)
    user = models.OneToOneField(User, models.SET_DEFAULT, default=None)
    name = models.CharField(max_length=255, default=None)
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
    user = models.OneToOneField(User, models.SET_DEFAULT, default=None)
    objects=models.Manager()


    def __str__(self):
        return self.user.username




class Pharmacy(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    license_no=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    contact_no=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    added_on=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class PharmacyBranch(models.Model):
    id=models.AutoField(primary_key=True)
    name_of_pharmacy = models.CharField(max_length=255)
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
    mfg_date=models.DateField()
    description=models.CharField(max_length=255)
    attention=models.CharField(max_length=255)
    frequecy=models.CharField(max_length=255)
    composition=models.CharField(max_length=255)
    notes=models.CharField(max_length=255)
    added_on=models.DateTimeField(auto_now_add=True)
    edited_on=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

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

class Prescription(models.Model):
    id = models.AutoField(primary_key=True)
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
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name

class Advertisement(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name