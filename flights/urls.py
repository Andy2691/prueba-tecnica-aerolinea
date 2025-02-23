from django.urls import path
from .views import FlightListView, flights_list

urlpatterns = [
    path("", flights_list, name="flights_home"),  # 🔹 Página HTML
    path("api/", FlightListView.as_view(), name="flights_api"),  # 🔹 API REST
]
