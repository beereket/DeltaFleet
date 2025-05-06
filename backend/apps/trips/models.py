from django.db import models
from fleet.models import Vehicle
from users.models import User

class Trip(models.Model):
    driver = models.ForeignKey(User, related_name="trips", on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, related_name="trips", on_delete=models.CASCADE)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    estimated_distance = models.FloatField()  # В километрах
    estimated_duration = models.FloatField()  # В часах
    status = models.CharField(max_length=20, choices=[('assigned', 'Assigned'), ('completed', 'Completed')], default='assigned')

    def __str__(self):
        return f"Trip {self.id} from {self.origin} to {self.destination}"
