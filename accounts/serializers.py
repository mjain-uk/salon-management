from rest_framework import serializers
from accounts.models import CustomUser
from django.contrib.auth import authenticate
from accounts.utils import AccountActivationUtils

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'id']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}, 'id':{'read_only':True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data, is_active=False)
        AccountActivationUtils.send_activation_email(user, self.context['request'])
        return user
    
    def to_representation(self, instance):
        """Overriding to remove Password Field when returning Data"""
        ret = super().to_representation(instance)
        ret.pop('password', None)
        return ret

class LoginAuthSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(username = email, password = password)
            if not user:
                raise serializers.ValidationError('Invalid credentials. Please try again.')
        else:
            raise serializers.ValidationError('Must include "email" and "password".')
        data['user'] = user
        return data
