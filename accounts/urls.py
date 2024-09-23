from django.urls import path,include
from rest_framework import routers
from accounts.views import UserRegistrationCreateView,UsersListView,LoginUsingAuthToken,ActivateAccountView

router = routers.DefaultRouter()

urlpatterns = [
    path('signup/',UserRegistrationCreateView.as_view()),
    path('users/',UsersListView.as_view()),
    path('login/', LoginUsingAuthToken.as_view()),
     path('activate/<uidb64>/<token>/', ActivateAccountView.as_view(), name='activate'),
    ]

urlpatterns+=router.urls
