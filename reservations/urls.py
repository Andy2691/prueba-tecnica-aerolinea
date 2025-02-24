from django.urls import path
from .views import my_reservations, cancel_reservation, create_reservation

urlpatterns = [
    path("", my_reservations, name="reservations_home"),
    path("create/", create_reservation, name="create_reservation"),
    path(
        "cancel/<int:pk>/", cancel_reservation, name="cancel_reservation"
    ),  # 🔥 Asegúrate de que esté correcta
]
