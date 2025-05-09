from django.db import models

# Create your models here.
from logistics.models import DeliveryTask

class VehicleLocation(models.Model):
    delivery_task = models.ForeignKey(DeliveryTask, on_delete=models.CASCADE, related_name='locations')
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    speed = models.FloatField(null=True, blank=True)  # km/h
    heading = models.FloatField(null=True, blank=True)  # degrees

    def __str__(self):
        return f"{self.delivery_task.task_id} @ {self.timestamp}"

class Geofence(models.Model):
    name = models.CharField(max_length=100)
    center_lat = models.FloatField()
    center_lng = models.FloatField()
    radius_meters = models.FloatField()
    delivery_task = models.ForeignKey(DeliveryTask, on_delete=models.CASCADE, related_name='geofences')

    def __str__(self):
        return f"{self.name} ({self.radius_meters}m)"

class GeofenceEvent(models.Model):
    EVENT_CHOICES = [
        ('ENTER', 'Entered'),
        ('EXIT', 'Exited')
    ]

    geofence = models.ForeignKey(Geofence, on_delete=models.CASCADE)
    vehicle_location = models.ForeignKey(VehicleLocation, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=10, choices=EVENT_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.geofence.name} {self.event_type} at {self.timestamp}"