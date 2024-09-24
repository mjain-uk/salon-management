from django.shortcuts import render
from rest_framework import generics
from appointments.serializers import AppointmentSerializer
from appointments.models import Appointment
from rest_framework.permissions import IsAdminUser, IsAuthenticated

# Create your views here.
class AppointmentView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     return Appointment.objects.first()