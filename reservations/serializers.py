from rest_framework import serializers
from .models import Reservation
from flights.models import Flight  # 🔹 Importamos Flight para validar la relación


class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )  # 🔹 Se asigna automáticamente el usuario autenticado

    flight_details = (
        serializers.SerializerMethodField()
    )  # 🔹 Agrega detalles del vuelo en la respuesta

    class Meta:
        model = Reservation
        fields = ["id", "user", "flight", "flight_details", "created_at"]
        read_only_fields = [
            "id",
            "created_at",
        ]  # 🔹 `id` y `created_at` solo de lectura

    def get_flight_details(self, obj):
        """Devuelve información más detallada del vuelo en la respuesta JSON"""
        return {
            "id": obj.flight.id,
            "origin": obj.flight.origin,
            "destination": obj.flight.destination,
            "date": obj.flight.date.strftime("%Y-%m-%d %H:%M:%S"),
        }

    def validate_flight(self, value):
        """Evita que un usuario reserve el mismo vuelo más de una vez"""
        user = self.context["request"].user
        if Reservation.objects.filter(user=user, flight=value).exists():
            raise serializers.ValidationError("Ya tienes una reserva para este vuelo.")
        return value
