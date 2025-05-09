from django.db import models
from fleet.models import Vehicle
from django.contrib.auth import get_user_model

User = get_user_model()

class DriverProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    license_number = models.CharField(max_length=100)
    license_expiry = models.DateField()
    address = models.TextField(blank=True, null=True)
    assigned_vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.license_number}"

class DriverAssignment(models.Model):
    driver = models.ForeignKey(DriverProfile, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.driver.user.get_full_name()} - {self.vehicle.vehicle_number}"