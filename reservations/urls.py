from django.urls import path
from .views import ReservationListView, my_reservations

urlpatterns = [
    path("", my_reservations, name="reservations_home"),  # 🔹 Página HTML
    path("api/", ReservationListView.as_view(), name="reservations_api"),  # 🔹 API REST
]
