from django.db import models
from django.core.exceptions import ValidationError


def validate_different_origin_destination(value):
    """🔹 Valida que el origen y destino no sean iguales"""
    if value["origin"] == value["destination"]:
        raise ValidationError("El origen y destino no pueden ser iguales.")


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Flight(models.Model):
    origin = models.ForeignKey(
        City, related_name="origin_flights", on_delete=models.CASCADE
    )
    destination = models.ForeignKey(
        City, related_name="destination_flights", on_delete=models.CASCADE
    )
    date = models.DateTimeField()
    available_seats = models.IntegerField()

    class Meta:
        ordering = ["date"]  # 🔹 Ordena los vuelos por fecha

    def clean(self):
        """🔹 Validaciones personalizadas al guardar un vuelo"""
        if self.origin == self.destination:
            raise ValidationError("El origen y destino no pueden ser iguales.")
        if self.available_seats < 0:
            raise ValidationError(
                "El número de asientos disponibles no puede ser negativo."
            )

    def __str__(self):
        return f"{self.origin.name} → {self.destination.name} ({self.date.strftime('%Y-%m-%d %H:%M')})"
