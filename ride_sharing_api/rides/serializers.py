from rest_framework import serializers
from .models import Ride


class RideSerializer(serializers.ModelSerializer):
    class Meta:
        """
        Meta class defines the model and fields to be serialized
        """

        model = Ride

        fields = "__all__"

        read_only_fields = (
            "id",
            "rider",
            "driver",
            "status",
            "created_at",
            "updated_at",
        )


    def validate(self, data):
        if not data.get("pickup_location"):
            raise serializers.ValidationError("Pickup location is required")
        if not data.get("dropoff_location"):
            raise serializers.ValidationError("Dropoff location is required")
        return data
