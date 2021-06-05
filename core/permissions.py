from rest_framework.permissions import BasePermission



class IsPharmacyOwrner(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_type == 3:
            return True
        else:
            return False


class IsPharmacist(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_type == 2:
            return True
        else:
            return False

class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_type == 3:
            return True
        else:
            return False
        

# class IsAssigned(permissions.BasePermission): 
#     """
#     Only person who assigned has permission
#     """

#     def has_object_permission(self, request, view, obj):
# 		# check if user who launched request is object owner 
#         if obj.assigned_to == request.user: 
#             return True
#         else:
#             return False