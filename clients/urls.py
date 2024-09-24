from django.urls import include, path
from rest_framework import routers

from clients.views import ClientRegistrationCreateView

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('client-profile/',ClientRegistrationCreateView.as_view()),
]