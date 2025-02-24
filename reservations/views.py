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
@login_required(
    login_url="/users/login/"
)  # 🔥 Redirigir a login si no está autenticado
def my_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(
        request, "reservations/my_reservations.html", {"reservations": reservations}
    )


# 🔹 API para cancelar reservas
@api_view(["DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def cancel_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
    reservation.delete()
    return JsonResponse({"message": "Reserva cancelada correctamente."}, status=200)


# 🔹 Vista HTML para crear una reserva desde Flights
@login_required(
    login_url="/users/login/"
)  # 🔥 Solo usuarios autenticados pueden reservar
def create_reservation(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "Debes iniciar sesión para hacer una reserva.")
            return redirect("user_login")

        flight_id = request.POST.get("flight")
        flight = get_object_or_404(Flight, id=flight_id)

        # Verificar si el usuario ya tiene una reserva para este vuelo
        if Reservation.objects.filter(user=request.user, flight=flight).exists():
            messages.error(request, "Ya tienes una reserva para este vuelo.")
            return redirect("reservations_home")

        # Crear la reserva si hay asientos disponibles
        if flight.available_seats > 0:
            Reservation.objects.create(user=request.user, flight=flight)
            messages.success(request, "Reserva creada exitosamente.")
        else:
            messages.error(request, "No hay asientos disponibles.")

    return redirect("reservations_home")
