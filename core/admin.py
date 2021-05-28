from django.contrib import admin
from .models import PharmacistProfile, PharmacyOwnerProfile, Branch, Pharmacy,PharmacyBranch,Product,Activity,Messages,Prescription,Report,Advertisement
# Register your models here.

admin.site.register(PharmacyOwnerProfile)
admin.site.register(PharmacistProfile)
admin.site.register(Branch)
admin.site.register(Pharmacy)
admin.site.register(PharmacyBranch)
admin.site.register(Product)
admin.site.register(Activity)
admin.site.register(Messages)
admin.site.register(Prescription)
admin.site.register(Report)
admin.site.register(Advertisement)

