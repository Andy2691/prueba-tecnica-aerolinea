from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from .models import Reservation
from .serializers import ReservationSerializer
from flights.models import Flight


# 🔹 API REST para listar y crear reservas (Solo usuarios autenticados)
@api_view(["GET", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def reservation_list_create(request):
    if request.method == "POST":
        flight_id = request.data.get("flight")

        if not flight_id:
            return JsonResponse(
                {"error": "Debes seleccionar un vuelo válido."}, status=400
            )

        flight = get_object_or_404(Flight, id=flight_id)

        # Crear reserva y asignar usuario autenticado
        reservation = Reservation.objects.create(user=request.user, flight=flight)
        return JsonResponse(
            {
                "message": "Reserva creada exitosamente.",
                "reservation_id": reservation.id,
            },
            status=201,
        )

    # Si es GET, devolvemos la lista de reservas del usuario
    reservations = Reservation.objects.filter(user=request.user).values(
        "id", "flight__origin", "flight__destination", "created_at"
    )
    return JsonResponse(list(reservations), safe=False)


# 🔹 API REST para cancelar reserva con autenticación por sesión
@api_view(["DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def cancel_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
    reservation.delete()
    return JsonResponse({"message": "Reserva cancelada correctamente."}, status=200)


# 🔹 Vista HTML para crear una reserva
@login_required
def create_reservation(request):
    if request.method == "POST":
        flight_id = request.POST.get("flight")

        if not flight_id:
            messages.error(request, "Debes seleccionar un vuelo válido.")
            return redirect("reservations_home")

        flight = get_object_or_404(Flight, id=flight_id)
        Reservation.objects.create(user=request.user, flight=flight)
        messages.success(request, "Reserva creada exitosamente.")

    return redirect("reservations_home")


# 🔹 Página HTML para mostrar reservas y formulario de creación
@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    flights = Flight.objects.all()

    return render(
        request,
        "reservations/my_reservations.html",
        {"reservations": reservations, "flights": flights},
    )
