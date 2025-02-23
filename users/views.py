from django.shortcuts import render, redirect
from rest_framework import generics
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .serializers import UserSerializer

User = get_user_model()


# API REST para registro de usuarios
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Página HTML con formulario de registro
def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Verificar si el usuario ya existe
        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya está en uso.")
            return redirect("register_form")

        if User.objects.filter(email=email).exists():
            messages.error(request, "El correo electrónico ya está registrado.")
            return redirect("register_form")

        # Crear usuario con nombre y apellido
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.save()

        messages.success(request, "¡Registro exitoso! Ahora puedes iniciar sesión.")
        return redirect("login_form")  # Redirigir a la página de login

    return render(request, "users/register.html")


# Página HTML con formulario de inicio de sesión
def login_view(request):
    return render(request, "users/login.html")


# API REST para autenticación manual (sin JWT)
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"message": "Login exitoso"})
        else:
            return JsonResponse({"error": "Credenciales inválidas"}, status=400)
