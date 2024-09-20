from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from accounts.models import CustomUser
from accounts.serializers import CustomUserSerializer,LoginAuthSerializer

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


class LoginUsingAuthToken(ObtainAuthToken):
    
    serializer_class = LoginAuthSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
