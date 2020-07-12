from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """Allow Users To Update Their Own Status"""

    def has_object_permission(self, request, view, obj):
        """Check The User Is Trying To Update Their Own Status"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id