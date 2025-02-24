from django.contrib import admin
from django.urls import path, include
from airline_system.views import home  # 🔥 Importa la vista home

urlpatterns = [
    path("", home, name="home"),  # Ruta para la página principal
    path("admin/", admin.site.urls),  # Panel de administración
    path("users/", include("users.urls")),  # URLs de usuarios (login, registro, etc.)
    path("flights/", include("flights.urls")),  # URLs de vuelos
    path("reservations/", include("reservations.urls")),  # URLs de reservas
]
