from django.db import models

# Create your models here.
from fleet.models import Vehicle
from drivers.models import DriverProfile

class DeliveryTask(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ASSIGNED', 'Assigned'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    task_id = models.CharField(max_length=100, unique=True)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    scheduled_time = models.DateTimeField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, blank=True)
    driver = models.ForeignKey(DriverProfile, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.task_id} - {self.status}"

class Route(models.Model):
    delivery_task = models.OneToOneField(DeliveryTask, on_delete=models.CASCADE)
    distance_km = models.FloatField()
    estimated_time_minutes = models.IntegerField()
    route_points = models.JSONField()  # List of lat/lng points

    def __str__(self):
        return f"Route for {self.delivery_task.task_id}"

class Waypoint(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='waypoints')
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    sequence = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.sequence})"
