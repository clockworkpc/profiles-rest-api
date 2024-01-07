from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit his own profile"""

    # correctly named method
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit his own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

    # previously incorrectly named method (missing an underscore)
    def has_objectpermission(self, request, view, obj):
        """Check user is trying to edit his own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update his own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
