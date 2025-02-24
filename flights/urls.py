from django.urls import path
from .views import flights_list, FlightListView, FlightDetailView

urlpatterns = [
    path("", flights_list, name="flights_home"),  # Página principal de vuelos
    path("api/", FlightListView.as_view(), name="flights_api"),  # API de vuelos
    path(
        "api/<int:pk>/", FlightDetailView.as_view(), name="flight_detail"
    ),  # API vuelo individual
]
