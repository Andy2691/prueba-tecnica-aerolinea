from django.db import models
from django.contrib.auth import get_user_model
from flights.models import Flight

User = get_user_model()


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
