from rest_framework import serializers
from .models import Ride


class RideSerializer(serializers.ModelSerializer):
    class Meta:
        """
        Meta class defines the model and fields to be serialized 
        """
        model = Ride

        # Serialize all fields from the Ride model
        fields = "__all__"

        # These fields are read-only and cannot be modified by the client.
        # They are controlled internally by the backend logic.
        read_only_fields = (
            "id",                   # Auto generated primary key 
            "rider",                # Automatically set from logged-in user
            "driver",               # Assigned when a driver accepts the ride 
            "status",               # Managed by ride life cycle APIs 
            "created_at",           # Automatically set when ride is created 
            "updated_at",           # Automatically updated on every save   
            "current_location",     # Updated only via tracking API
        )
