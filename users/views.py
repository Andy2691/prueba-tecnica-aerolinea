from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from .serializers import UserSerializer

User = get_user_model()


# 🔹 API REST para registro de usuarios
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# 🔹 Página HTML con formulario de registro
def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya está en uso.")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "El correo electrónico ya está registrado.")
            return redirect("register")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.save()

        messages.success(request, "¡Registro exitoso! Ahora puedes iniciar sesión.")
        return redirect("user_login")  # 🔥 Redirige correctamente al login

    return render(request, "users/register.html")


# 🔹 Página HTML con formulario de inicio de sesión
def login_view(request):
    return render(request, "users/login.html")


# 🔹 API para iniciar sesión (corrige la autenticación)
@csrf_exempt  # Si usas Django REST Framework, prueba quitándolo si no es necesario
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        print(
            f"Intentando iniciar sesión con: {username} - {password}"
        )  # 🔍 Depuración

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Inicio de sesión exitoso.")
            return redirect("reservations_home")  # 🔥 Redirige a la página de reservas
        else:
            messages.error(request, "Credenciales inválidas. Intenta de nuevo.")
            return redirect("user_login")  # 🔥 Redirige al login si falla

    return render(request, "users/login.html")  # 🔥 Asegura que el login se renderiza


# 🔹 API REST para obtener información del usuario autenticado
@api_view(["GET"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user
    return JsonResponse(
        {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }
    )


# 🔹 API para cerrar sesión (logout corregido)
@api_view(["POST"])
def user_logout(request):  # 🔥 Cambio el nombre para que coincida con las URLs
    logout(request)
    messages.success(request, "Sesión cerrada correctamente.")
    return redirect("user_login")  # 🔥 Redirige a la página de login
