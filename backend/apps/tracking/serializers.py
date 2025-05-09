from rest_framework import serializers
from .models import VehicleLocation, Geofence, GeofenceEvent
from logistics.models import DeliveryTask

class VehicleLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleLocation
        fields = '__all__'

class GeofenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geofence
        fields = '__all__'

class GeofenceEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeofenceEvent
        fields = '__all__'
