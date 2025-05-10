from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import DriverApplication

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.role = 'GUEST'
        user.save()
        return user

class DriverApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverApplication
        fields = ['id', 'license_number', 'experience_years', 'additional_info', 'status', 'submitted_at']

class DriverApplicationDecisionSerializer(serializers.Serializer):
    manager_response = serializers.CharField(required=False)


