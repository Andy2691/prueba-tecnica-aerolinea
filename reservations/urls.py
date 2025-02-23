from django.urls import path
from .views import ReservationListView

urlpatterns = [
    path("reservations/", ReservationListView.as_view(), name="reservation-list"),
]
