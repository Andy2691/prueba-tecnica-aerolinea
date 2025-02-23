from django.urls import path
from .views import ReservationListView, my_reservations, cancel_reservation

urlpatterns = [
    path("", my_reservations, name="reservations_home"),  # 🔹 Página HTML
    path(
        "api/", ReservationListView.as_view(), name="reservations_api"
    ),  # 🔹 API REST (Listar/Crear reservas)
    path(
        "api/cancel/<int:pk>/", cancel_reservation, name="cancel_reservation"
    ),  # 🔹 API REST para cancelar reservas
]
