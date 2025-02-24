from rest_framework import serializers
from .models import Flight


class FlightSerializer(serializers.ModelSerializer):
    """Serializador para los vuelos con validaciones personalizadas"""

    class Meta:
        model = Flight
        fields = ["id", "origin", "destination", "date", "available_seats"]

    def validate(self, data):
        """🔹 Validaciones personalizadas antes de crear o actualizar un vuelo"""
        if data["available_seats"] < 0:
            raise serializers.ValidationError(
                {
                    "available_seats": "El número de asientos disponibles no puede ser negativo."
                }
            )
        if data["origin"] == data["destination"]:
            raise serializers.ValidationError(
                {"destination": "El origen y destino no pueden ser iguales."}
            )
        return data
