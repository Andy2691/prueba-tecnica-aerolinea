from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Reservation
from flights.models import Flight


# 🔹 Página HTML para mostrar reservas y permitir cancelación
@login_required
def my_reservations(request):
    """Muestra las reservas del usuario autenticado."""
    reservations = Reservation.objects.filter(user=request.user)

    return render(
        request,
        "reservations/my_reservations.html",
        {"reservations": reservations},
    )


# 🔹 API para cancelar reservas (corrigiendo el formato JSON)
@api_view(["DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def cancel_reservation(request, pk):
    try:
        reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
        reservation.delete()
        return JsonResponse({"message": "Reserva cancelada correctamente."}, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


# 🔹 Vista HTML para crear una reserva desde Flights
@login_required
def create_reservation(request):
    """Evita duplicados y crea una reserva solo si no existe."""
    if request.method == "POST":
        flight_id = request.POST.get("flight")

        if not flight_id:
            messages.error(request, "Debes seleccionar un vuelo válido.")
            return redirect("flights_home")

        flight = get_object_or_404(Flight, id=flight_id)

        # Verificar si ya existe una reserva para este usuario y vuelo
        existing_reservation = Reservation.objects.filter(
            user=request.user, flight=flight
        ).exists()

        if existing_reservation:
            messages.error(request, "Ya tienes una reserva para este vuelo.")
            return redirect("reservations_home")

        if flight.available_seats > 0:
            Reservation.objects.create(user=request.user, flight=flight)
            messages.success(request, "Reserva creada exitosamente.")
        else:
            messages.error(request, "No hay asientos disponibles.")

    return redirect("reservations_home")  # Redirige a la lista de reservas
