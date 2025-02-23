from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterUserView, register, login_view, user_login

urlpatterns = [
    # 🔹 Vistas HTML (Para autenticación basada en sesión)
    path("register/", register, name="register_form"),  # Página HTML para registro
    path("login/", login_view, name="login_form"),  # Página HTML para login
    # 🔹 API REST (Para autenticación manual sin JWT)
    path(
        "register/api/", RegisterUserView.as_view(), name="register_api"
    ),  # API de registro
    path(
        "login/api/", user_login, name="user_login"
    ),  # API de login (Devuelve sesión + JWT)
    # 🔹 API REST con JWT (Para autenticación con tokens)
    path(
        "token/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),  # Obtener tokens
    path(
        "token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),  # Refrescar token
]
