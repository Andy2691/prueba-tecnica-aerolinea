from django.urls import path
from .views import RegisterUserView, register

urlpatterns = [
    path("register/", register, name="register_form"),  # 🔹 Formulario HTML
    path(
        "register/api/", RegisterUserView.as_view(), name="register_api"
    ),  # 🔹 API REST
]
