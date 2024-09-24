from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.utils import account_activation_token
from accounts.serializers import CustomUserSerializer,LoginAuthSerializer, ResetPasswordSerializer, SetNewPasswordSerializer



User = get_user_model()

# Create your views here.

class UserRegistrationCreateView(CreateAPIView):
    """Generic View for Creating User Profiles"""
    serializer_class = CustomUserSerializer
    permission_class = [AllowAny]

class UsersListView(ListAPIView):
    """Generic View for Listing User Profiles"""
    queryset = User.objects.all()
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

class ActivateAccountView(APIView):

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            # Decode user ID
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({'error': 'Invalid token or user ID'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the token is valid
        if account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()

            # Activation successful
            return Response({'message': 'Account activated successfully!'}, status=status.HTTP_200_OK)
        else:
            # Token invalid
            return Response({'error': 'Activation link is invalid!'}, status=status.HTTP_400_BAD_REQUEST)

class ResetPasswordView(APIView):
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        return Response({'success': 'Password Reset link has been sent'}, status=status.HTTP_200_OK)

class PasswordResetConfirmView(APIView):

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            # Decode user ID
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(email=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({'error': 'Invalid token or user email'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the token is valid
        if account_activation_token.check_token(user, token):

            # Activation successful
            return Response({'message': 'Token verified successfully!'}, status=status.HTTP_200_OK)
        else:
            # Token invalid
            return Response({'error': 'Reset link is invalid or has expired.'}, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, uidb64, token):
        try:
            # Decode user ID
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(email=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({'error': 'Invalid token or user email'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not account_activation_token.check_token(user, token):
            return Response({'error': 'Reset link is invalid or has expired.'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = SetNewPasswordSerializer(data = request.data)
        if serializer.is_valid():
            new_password = serializer.validated_data['password']
            user.set_password(new_password)
            user.save()

            return Response({'message': 'Password reset successful!'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        