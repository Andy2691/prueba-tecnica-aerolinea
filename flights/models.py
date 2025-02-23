from django.db import models


class Flight(models.Model):
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date = models.DateTimeField()
    available_seats = models.IntegerField()

    def __str__(self):
        return f"{self.origin} → {self.destination} ({self.date})"
