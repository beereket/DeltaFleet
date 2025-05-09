from rest_framework import serializers
from .models import DeliveryTask, Route, Waypoint
from fleet.models import Vehicle
from drivers.models import DriverProfile

class DeliveryTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryTask
        fields = '__all__'

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'

class WaypointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waypoint
        fields = '__all__'
