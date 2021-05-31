from rest_framework.permissions import BasePermission



class IsPharmacyOwrner(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == "pharmacyowner"


class IsPharmacist(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == "phamacist"

class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == "customer"