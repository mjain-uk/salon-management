from rest_framework import serializers
from services.models import Service

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id','name', 'price', 'category']