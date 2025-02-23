from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework import generics
from .models import Reservation
from .serializers import ReservationSerializer


# 🔹 API REST para listar y crear reservas
class ReservationListView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


# 🔹 API REST para cancelar una reserva
def cancel_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    reservation.delete()
    return JsonResponse({"message": "Reserva cancelada correctamente."})


# 🔹 Página HTML para mostrar reservas
def my_reservations(request):
    reservations = Reservation.objects.all()  # Obtiene todas las reservas
    return render(
        request, "reservations/my_reservations.html", {"reservations": reservations}
    )
