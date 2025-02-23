from django.shortcuts import render


def home(request):
    return render(request, "index.html")  # 🔹 Renderiza la página de inicio
