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
    objects=models.Manager()


    def __str__(self):
        return self.user.username

class Branch(models.Model):
    name = models.CharField(max_length=200)
    objects=models.Manager()

    def __str__(self):
        return self.name


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
    name=models.CharField(max_length=255)
    license_no=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
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
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name

class Messages(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.CharField(max_length=255)
    reciever = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return f'{self.sender} sending message to {self.reciever}'

class Prescription(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
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