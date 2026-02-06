from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Ride(models.Model):
    STATUS_CHOICES = [
        ("REQUESTED", "Requested"),
        ("ACCEPTED", "Accepted"),
        ("STARTED", "Started"),
        ("COMPLETED", "Completed"),
        ("CANCELED", "Canceled"),
    ]

    rider = models.ForeignKey(User, related_name="rides", on_delete=models.CASCADE)
    driver = models.ForeignKey(
        User, related_name="drives", null=True, blank=True, on_delete=models.SET_NULL
    )
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    current_location = models.CharField(max_length=255)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="REQUESTED"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ride {self.id} - {self.status}"
