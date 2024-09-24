from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from appointments.serializers import AppointmentSerializer
from appointments.models import Appointment
from salonmanagement.permissions import IsAdminOrRelatedClient, IsAuthenticatedAndActive
from clients.models import Client
from django.shortcuts import get_object_or_404

# Create your views here.
class AppointmentView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAdminOrRelatedClient, IsAuthenticatedAndActive, ]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Appointment.objects.all()
        client = get_object_or_404(Client, user=self.request.user)            
        return Appointment.objects.filter(client=client)