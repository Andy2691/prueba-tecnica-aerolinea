from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    # 🔹 Eliminamos los campos `groups` y `user_permissions` porque ya existen en `AbstractUser`

    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
    ]  # 🔹 Pedimos nombre y apellido en lugar de email

    def __str__(self):
        return self.username  # 🔹 Muestra el username en el admin de Django
