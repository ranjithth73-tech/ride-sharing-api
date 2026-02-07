from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Ride(models.Model):

    # All possible states of a ride during its lifecycle
    STATUS_CHOICES = [
        ("REQUESTED", "Requested"),  # Ride create by rider
        ("ACCEPTED", "Accepted"),    # Driver Accept the ride
        ("STARTED", "Started"),      # Ride has started
        ("COMPLETED", "Completed"),  # Ride finished successfully
        ("CANCELED", "Canceled"),    # Ride canceled driver or rider
    ]

    # User who request to the ride
    rider = models.ForeignKey(User, related_name="rides", on_delete=models.CASCADE)

    # User who accepts and drives the ride (driver)
    # SET_NULL allows the rides exits the even if the driver removed
    driver = models.ForeignKey(
        User, related_name="drives", null=True, blank=True, on_delete=models.SET_NULL
    )

    # Location Where the rider will be picked up
    pickup_location = models.CharField(max_length=250)

    # Destination location of the ride
    dropoff_location = models.CharField(max_length=250)

    # Current location of the ride  (Used for real-time tracking simulation)
    current_location = models.CharField(max_length=250)

    # Current status of the ride 
    # Default is REQUIRED when a ride is first created
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="REQUESTED"
    )

    # Timestamp when the ride was created
    created_at = models.DateTimeField(auto_now_add=True)

    # TImestamp updated whenever the ride details change 
    updated = models.DateTimeField(auto_now=True)


    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    
    def __str__(self):
        # Return the human readable fille 
        return f"Ride {self.id} - {self.status}"
