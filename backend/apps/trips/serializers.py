from rest_framework import serializers
from .models import Trip
from fleet.serializers import VehicleSerializer
from users.serializers import UserSerializer

class TripSerializer(serializers.ModelSerializer):
    driver = UserSerializer()
    vehicle = VehicleSerializer()

    class Meta:
        model = Trip
        fields = ('id', 'driver', 'vehicle', 'origin', 'destination', 'estimated_distance', 'estimated_duration', 'status')
