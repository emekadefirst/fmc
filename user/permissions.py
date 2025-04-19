from .models import User
from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.is_superuser)
    

class IsAdminOrCleaner(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.is_cleaner and request.user.is_superuser)
    

class IsVerified(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.is_verified)

class IsActive(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.is_active)
    

