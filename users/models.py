from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",  # 🔧 Se cambia el related_name para evitar conflictos
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions_set",  # 🔧 Se cambia el related_name
        blank=True,
    )

    REQUIRED_FIELDS = ["email"]
