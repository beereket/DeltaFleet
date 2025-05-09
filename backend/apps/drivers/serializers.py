from rest_framework import serializers
from .models import DriverProfile, DriverAssignment

class DriverProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverProfile
        fields = '__all__'

class DriverAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverAssignment
        fields = '__all__'
