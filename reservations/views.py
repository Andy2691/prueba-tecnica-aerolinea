from django.shortcuts import render
from rest_framework import generics
from .models import Reservation
from .serializers import ReservationSerializer


# API REST para obtener la lista de reservas
class ReservationListView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


# Página HTML para mostrar reservas
def my_reservations(request):
    return render(request, "reservations/my_reservations.html")
