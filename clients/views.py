from rest_framework import generics
from clients.models import Client
from clients.serializers import ClientSerializer
from rest_framework.permissions import IsAuthenticated
from salonmanagement.permissions import IsAdminOrRelatedClient


# Create your views here.
class ClientRegistrationCreateView(generics.ListCreateAPIView):
    """Generic View for Creating User Profiles"""
    serializer_class = ClientSerializer
    permission_class = [IsAuthenticated, IsAdminOrRelatedClient]
    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return Client.objects.all()
        return Client.objects.filter(user=user)
    
    
