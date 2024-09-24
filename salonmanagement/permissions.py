from rest_framework.permissions import IsAuthenticated, BasePermission

class IsAuthenticatedAndActive(IsAuthenticated):
    """
    Custom permission that allows access only to authenticated and active users.
    """
    def has_permission(self, request, view):
        # First, check if the user is authenticated using the parent class method
        is_authenticated = super().has_permission(request, view)
        
        # Then, add a check for the 'is_active' flag
        return is_authenticated and request.user.is_active

class IsAdminOrRelatedClient(BasePermission):
    """
    Custom permission to allow admin users to access everything,
    and regular users to access only their own objects.
    """
    def has_permission(self, request, view):
        # Allow access if the user is authenticated
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Admins can access any object
        if request.user.is_staff or request.user.is_superuser:
            return True
        # Regular users can only access their own client profile
        return obj.user == request.user