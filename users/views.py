from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model()


# API REST para registro de usuarios
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Página HTML con formulario de registro
def register(request):
    return render(request, "users/register.html")
