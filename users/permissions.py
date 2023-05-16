from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAccountOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.method in SAFE_METHODS:
            return request.user == obj
        return True
