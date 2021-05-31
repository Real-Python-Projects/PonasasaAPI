from rest_framework.permissions import BasePermission



class IsPharmacyOwrner(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.user_type == "pharmacyowner"


class IsPharmacist(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.user_type == "phamacist"

class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.user_type == "customer"