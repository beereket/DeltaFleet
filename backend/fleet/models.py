from django.db import models

# Create your models here.
class VehicleType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=50, unique=True)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.SET_NULL, null=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    capacity_kg = models.FloatField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.vehicle_number} - {self.brand} {self.model}"

class MaintenanceRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='maintenance_records')
    maintenance_type = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField(blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.maintenance_type} - {self.vehicle.vehicle_number}"

class FuelLog(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='fuel_logs')
    date = models.DateField()
    amount_liters = models.FloatField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    odometer_reading_km = models.FloatField()

    def __str__(self):
        return f"{self.date} - {self.vehicle.vehicle_number}"