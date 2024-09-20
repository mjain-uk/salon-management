from django.urls import path,include
from rest_framework import routers
from accounts.views import UserRegistrationCreateView,UsersListView

router = routers.DefaultRouter()

urlpatterns = [
    path('signup/',UserRegistrationCreateView.as_view()),
    path('users/',UsersListView.as_view()),
    ]


urlpatterns+=router.urls
