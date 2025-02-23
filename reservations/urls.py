from django.urls import path
from .views import (
    my_reservations,
    create_reservation,
    reservation_list_create,
    cancel_reservation,
)

urlpatterns = [
    path("", my_reservations, name="reservations_home"),  # 🔹 Página HTML con reservas
    path(
        "create/", create_reservation, name="create_reservation"
    ),  # 🔹 Formulario HTML para crear reservas
    path(
        "api/", reservation_list_create, name="reservations_api"
    ),  # 🔹 API REST para listar/crear reservas
    path(
        "api/cancel/<int:pk>/", cancel_reservation, name="cancel_reservation"
    ),  # 🔹 API REST para cancelar reservas
]
