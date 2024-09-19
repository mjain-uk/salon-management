from django.urls import path, include
from rest_framework import routers
from appointments.views import AppointmentViewSet

router = routers.DefaultRouter()

router.register(r'appointments', AppointmentViewSet)

urlpatterns = [path('', include(router.urls))]
