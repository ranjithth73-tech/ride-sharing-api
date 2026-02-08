from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Ride
from .serializers import RideSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from .utils import calculate_distance
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied


# Create your views here.

User = get_user_model()


class RideViewSet(ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.is_driver:
            raise PermissionDenied("Drivers cannot create rides")
        serializer.save(rider=self.request.user)

        # Driver Accept the ride

    @action(detail=True, methods=["post"])
    def accept(self, request, pk=None):
        ride = self.get_object()
        if not request.user.is_driver:
            return Response(
                {"error": "Only drivers can accept the rides"},
                status=status.HTTP_403_FORBIDDEN,
            )
        if ride.status != "REQUESTED":
            return Response({"error": "Ride not available"}, status=400)
        ride.driver = request.user
        ride.status = "ACCEPTED"
        ride.save()
        return Response({"message": "Ride accepted"}, status=200)

    # Start the ride
    @action(detail=True, methods=["post"])
    def start(self, request, pk=None):
        ride = self.get_object()
        if ride.driver != request.user:
            return Response({"error": "Only driver can start ride"}, status=403)

        if ride.status != "ACCEPTED":
            return Response({"message": "Ride is not accepted"}, status=400)

        ride.status = "STARTED"
        ride.save()
        return Response({"message": "Ride started"}, status=200)

    # Complete the ride
    @action(detail=True, methods=["post"])
    def completed(self, request, pk=None):
        ride = self.get_object()
        if ride.driver != request.user:
            return Response({"error": "Only driver can complete the ride"}, status=403)

        if ride.status != "STARTED":
            return Response({"error": "RIde is not started"}, status=400)
        ride.status = "COMPLETED"
        ride.save()
        return Response({"message": "Ride completed"}, status=200)

        # Cancel ride

    @action(detail=True, methods=["post"])
    def canceled(self, request, pk=None):
        ride = self.get_object()
        if request.user.is_driver:
            return Response(
                {"error": "Driver cannot cancel rides"},
                status=status.HTTP_403_FORBIDDEN,
            )

        if ride.rider != request.user:
            return Response({"error": "Only rider can cancel ride"}, status=403)

        if ride.status in ["COMPLETED", "CANCELED"]:
            return Response(
                {"error": "Ride Cannot be canceled"}, status=status.HTTP_400_BAD_REQUEST
            )

        ride.status = "CANCELED"
        ride.save()
        return Response({"message": "RIde canceled"}, status=200)

    # Real Time tracking
    @action(detail=True, methods=["post"])
    def update_location(self, request, pk=None):
        ride = self.get_object()

        latitude = request.data.get("latitude")
        longitude = request.data.get("longitude")

        if latitude is None or longitude is None:
            return Response(
                {"error": "latitude and longitude are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        ride.current_latitude = latitude
        ride.current_longitude = longitude
        ride.save()
        return Response(
            {
                "message": "Location Updated",
                "latitude": ride.current_latitude,
                "longitude": ride.current_longitude,
            },
            status=status.HTTP_200_OK,
        )

    @action(detail=True, methods=["get"])
    def location(self, request, pk=None):
        ride = self.get_object()
        return Response(
            {"latitude": ride.current_latitude, "longitude": ride.current_longitude},
            status=status.HTTP_200_OK,
        )

        # Driver Matching
    @action(detail=True, methods=["post"])
    def match_driver(self, request, pk=None):
        ride = self.get_object()

        # Only match if ride is still requested
        if ride.status != "REQUESTED":
            return Response(
                {"error": "Ride already matched or processed"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Find drivers with known locations
        drivers = User.objects.filter(is_driver=True)

        if not drivers.exists():
            return Response(
                {"error": "No available drivers"}, status=status.HTTP_404_NOT_FOUND
            )

        nearest_driver = None
        min_distance = float("inf")

        for driver in drivers:
            driver_lat = 12.9716
            driver_lon = 77.5946

            if ride.pickup_latitude is None or ride.pickup_longitude is None:
                continue

            distance = calculate_distance(
                ride.pickup_latitude,
                ride.pickup_longitude,
                driver_lat,
                driver_lon,
            )

            if distance < min_distance:
                min_distance = distance
                nearest_driver = driver

        if not nearest_driver:
            return Response(
                {"error": "No drivers available"}, status=status.HTTP_404_NOT_FOUND
            )

        # Assign driver
        ride.driver = nearest_driver
        ride.status = "ACCEPTED"
        ride.save()

        return Response(
            {
                "message": "Driver matched successfully",
                "driver_id": nearest_driver.id,
                "distance_km": round(min_distance, 2),
            },
            status=status.HTTP_200_OK,
        )
