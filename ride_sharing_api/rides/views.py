from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Ride
from .serializers import RideSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.


class RideViewSet(ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(rider=self.request.user)

    @action(detail=True, methods=["post"])
    def accept(self, request, pk=None):
        ride = self.get_object()
        ride.driver = request.user
        ride.status = "ACCEPTED"
        ride.save()
        return Response({"message": "Ride accepted"}, status=200)

    @action(detail=True, methods=["post"])
    def start(self, request, pk=None):
        ride = self.get_object()
        ride.status = "STARTED"
        ride.save()
        return Response({"message": "Ride started"}, status=200)

    @action(detail=True, methods=["post"])
    def completed(self, request, pk=None):
        ride = self.get_object()
        ride.status = "COMPLETED"
        ride.save()
        return Response({"message": "Ride completed"}, status=200)

    @action(detail=True, methods=["post"])
    def canceled(self, request, pk=None):
        ride = self.get_object()
        ride.status = "CANCELED"
        ride.save()
        return Response({"message": "RIde canceled"}, status=200)
