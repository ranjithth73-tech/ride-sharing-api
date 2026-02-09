from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class Ride(models.Model):

    STATUS_CHOICES = [
        ("REQUESTED", "Requested"),
        ("ACCEPTED", "Accepted"),
        ("STARTED", "Started"),
        ("COMPLETED", "Completed"),
        ("CANCELED", "Canceled"),
    ]

    rider = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="rides", on_delete=models.CASCADE
    )

    driver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="drives",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    pickup_location = models.CharField(max_length=250)
    dropoff_location = models.CharField(max_length=250)

    pickup_latitude = models.FloatField(null=True, blank=True)
    pickup_longitude = models.FloatField(null=True, blank=True)

    current_latitude = models.FloatField(null=True, blank=True)
    current_longitude = models.FloatField(null=True, blank=True)

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="REQUESTED"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # latitude = models.FloatField(null=True, blank=True)
    # longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Ride {self.id} - {self.status}"
