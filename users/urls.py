from django.urls import path
from .views import user_login, register, user_logout

urlpatterns = [
    path("login/", user_login, name="user_login"),  # URL para iniciar sesión
    path("register/", register, name="register"),  # URL para registro
    path("logout/", user_logout, name="user_logout"),  # URL para cerrar sesión
]
