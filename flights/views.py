from django.shortcuts import render
from rest_framework import generics
from .models import Flight, City
from .serializers import FlightSerializer


# 🔹 API REST para obtener la lista de vuelos con filtros
class FlightListView(generics.ListAPIView):
    serializer_class = FlightSerializer

    def get_queryset(self):
        """Permite buscar vuelos por origen, destino y fecha"""
        queryset = Flight.objects.all()
        origin = self.request.query_params.get("origin", None)
        destination = self.request.query_params.get("destination", None)
        date = self.request.query_params.get("date", None)

        if origin:
            queryset = queryset.filter(origin__name__icontains=origin)
        if destination:
            queryset = queryset.filter(destination__name__icontains=destination)
        if date:
            queryset = queryset.filter(date=date)

        return queryset


# 🔹 API REST para obtener un vuelo por ID
class FlightDetailView(generics.RetrieveAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


# 🔹 Página HTML para listar vuelos con búsqueda
# 🔹 Permite ver los vuelos sin estar autenticado
def flights_list(request):
    """Renderiza la lista de vuelos con filtros"""
    origin = request.GET.get("origin", "")
    destination = request.GET.get("destination", "")
    date = request.GET.get("date", "")

    cities = City.objects.all()
    flights = Flight.objects.all()

    if origin:
        flights = flights.filter(origin__name=origin)
    if destination:
        flights = flights.filter(destination__name=destination)
    if date:
        flights = flights.filter(date=date)

    return render(
        request,
        "flights/flights_list.html",
        {
            "flights": flights,
            "origin": origin,
            "destination": destination,
            "date": date,
            "cities": cities,
        },
    )
