from django.shortcuts import render
from rest_framework import generics
from .models import Flight
from .serializers import FlightSerializer


# API REST para obtener la lista de vuelos
class FlightListView(generics.ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


# Página HTML para listar vuelos
def flights_list(request):
    return render(request, "flights/flights_list.html")
