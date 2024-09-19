from django.shortcuts import render
from rest_framework import viewsets
from appointments.serializers import AppointmentSerializer
from appointments.models import Appointment

# Create your views here.
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
