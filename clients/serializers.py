from rest_framework import serializers
from clients.models import Client


class ClientSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)  # Custom field to get user's email
    class Meta:
        model = Client
        fields = ['id','user', 'first_name', 'last_name', 'email', 'preferences', 'notes']
        extra_kwargs = { 'id':{'read_only':True}}

        