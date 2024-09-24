from rest_framework import serializers
from appointments.models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'client', 'service', 'event_date', 'consultation_date', 'created_on']

