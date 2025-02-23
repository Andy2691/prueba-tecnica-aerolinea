from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterUserView, register, login_view, user_login

urlpatterns = [
    # 🔹 Páginas HTML
    path("register/", register, name="register_form"),  # Página HTML para registro
    path("login/", login_view, name="login_form"),  # Página HTML para login
    # 🔹 API REST
    path(
        "register/api/", RegisterUserView.as_view(), name="register_api"
    ),  # API de registro
    path("login/api/", user_login, name="user_login"),  # API de login manual (sin JWT)
    # 🔹 API JWT
    path(
        "token/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),  # Obtener access y refresh token
    path(
        "token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),  # Refrescar token
]
