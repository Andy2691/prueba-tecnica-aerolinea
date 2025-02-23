from django.contrib import admin
from django.urls import path, include
from .views import home  # 🔹 Importamos la vista de inicio

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),  # 🔹 Rutas de Usuarios
    path("flights/", include("flights.urls")),  # 🔹 Rutas de Vuelos
    path("reservations/", include("reservations.urls")),  # 🔹 Rutas de Reservas
    path("", home, name="home"),  # 🔹 Página principal
]
