from rest_framework import generics
from .models import Reservation
from .serializers import ReservationSerializer


class ReservationListView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
