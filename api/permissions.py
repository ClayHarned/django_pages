# api/permissions.py
from rest_framework import permissions

class IsProfileAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS are: GET, OPTIONS, HEAD
        if request.method in permissions.SAFE_METHODS:
            return True

        # Otherwise, only the tweet author can change a profile
        return obj.user == request.user
