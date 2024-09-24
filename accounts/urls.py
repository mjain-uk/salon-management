from django.urls import path,include
from rest_framework import routers
from accounts.views import UserRegistrationCreateView,UsersListView,LoginUsingAuthToken,ActivateAccountView, ResetPasswordView, PasswordResetConfirmView

router = routers.DefaultRouter()

urlpatterns = [
    path('signup/',UserRegistrationCreateView.as_view()),
    path('users/',UsersListView.as_view()),
    path('login/', LoginUsingAuthToken.as_view()),
    path('activate/<uidb64>/<token>/', ActivateAccountView.as_view(), name='activate'),
    path('password-reset/',ResetPasswordView.as_view(), name='password-reset' ),
    path('password-reset-confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(), name='password-reset-confirm')
    ]

urlpatterns+=router.urls
