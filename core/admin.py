# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import *
# Register your models here.




admin.site.site_title = "Ponasasa"
admin.site.site_header = "Ponasasa"



class PaymentTransactionAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "amount", "isFinished",
                    "isSuccessFull", "trans_id", 'date_created','date_modified')

admin.site.register(PaymentTransaction, PaymentTransactionAdmin)
admin.site.register(Wallet)

admin.site.register(PharmacyOwnerProfile)
admin.site.register(PharmacistProfile)
admin.site.register(CustomerProfile)
admin.site.register(Pharmacy)
admin.site.register(PharmacyBranch)
admin.site.register(Product)
admin.site.register(Activity)
admin.site.register(Messages)
admin.site.register(Prescription)
admin.site.register(Report)
admin.site.register(Advertisement)
admin.site.register(NotificationCustomer)
admin.site.register(NotificationPharmacist)

