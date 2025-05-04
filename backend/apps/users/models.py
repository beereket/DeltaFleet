from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('driver', 'Driver'),
        ('manager', 'Manager'),
    )
    role = models.CharField(max_length=20, choices=ROLES, default='driver')
