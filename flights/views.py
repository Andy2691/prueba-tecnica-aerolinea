from rest_framework import generics
from .models import Flight
from .serializers import FlightSerializer


class FlightListView(generics.ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
