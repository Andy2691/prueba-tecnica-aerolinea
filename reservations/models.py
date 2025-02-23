from django.db import models
from django.contrib.auth import get_user_model
from flights.models import Flight  # 🔹 Importamos el modelo Flight

User = get_user_model()


class Reservation(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reservations"
    )  # 🔹 Permite acceder a todas las reservas de un usuario fácilmente
    flight = models.ForeignKey(
        Flight, on_delete=models.CASCADE, related_name="reservations"
    )  # 🔹 Permite acceder a todas las reservas de un vuelo
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [
            "-created_at"
        ]  # 🔹 Ordena las reservas por fecha más reciente primero
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        unique_together = (
            "user",
            "flight",
        )  # 🔹 Evita que un usuario reserve el mismo vuelo más de una vez

    def __str__(self):
        return f"Reserva de {self.user.username} - Vuelo {self.flight.origin} → {self.flight.destination} ({self.created_at.strftime('%Y-%m-%d %H:%M:%S')})"
