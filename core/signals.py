
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
# from .models import PharmacyProfile, CustomUser,PharmacyOwnerProfile,PharmacistProfile
from .models import *

@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type==1:
            PharmacyOwnerProfile.objects.create(user=instance)
        if instance.user_type==2:
            PharmacyProfile.objects.create(user=instance)
        if instance.user_type==3:
            PharmacistProfile.objects.create(user=instance)
	
    
@receiver(post_save,sender=CustomUser)
def save_profile(sender,instance, **kwargs):
    if instance.user_type==1:
        instance.pharmacyownerprofile.save()
    if instance.user_type==2:
        instance.pharmacyprofile.save()
    if instance.user_type==3:
        instance.pharmacistprofile.save()
		




    