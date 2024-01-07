from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit his own profile"""

    def has_objectpermission(self, request, view, obj):
        """Check user is trying to edit his own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
