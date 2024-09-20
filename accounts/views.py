from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from accounts.models import CustomUser
from accounts.serializers import CustomUserSerializer

# Create your views here.

class UserRegistrationCreateView(CreateAPIView):
    """Generic View for Creating User Profiles"""
    serializer_class = CustomUserSerializer
    permission_class = [AllowAny]

class UsersListView(ListAPIView):
    """Generic View for Listing User Profiles"""
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_class = [AllowAny]

    

