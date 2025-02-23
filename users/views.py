from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
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
            return redirect("register_form")

        if User.objects.filter(email=email).exists():
            messages.error(request, "El correo electrónico ya está registrado.")
            return redirect("register_form")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.save()

        messages.success(request, "¡Registro exitoso! Ahora puedes iniciar sesión.")
        return redirect("login_form")

    return render(request, "users/register.html")


# 🔹 Página HTML con formulario de inicio de sesión
def login_view(request):
    return render(request, "users/login.html")


# 🔹 API REST para autenticación con sesiones
@csrf_exempt
@api_view(["POST"])
@authentication_classes([SessionAuthentication])
def user_login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)  # 🔥 Iniciar sesión con SessionAuthentication
        return JsonResponse({"message": "Login exitoso"})
    else:
        return JsonResponse({"error": "Credenciales inválidas"}, status=400)


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


# 🔹 API para cerrar sesión (logout)
@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def user_logout(request):
    """Cerrar sesión en Django"""
    request.session.flush()  # 🔥 Elimina la sesión del usuario
    return JsonResponse({"message": "Sesión cerrada correctamente"}, status=200)
