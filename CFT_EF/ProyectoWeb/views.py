from django.shortcuts import HttpResponse, redirect, render
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, "index.html")

def saludo(request):
    diccionario = {"Titulo": "Saludo de Bienvenida",
                    "saludo": "Bienvenidos estudiantes de la Universidad Nacional Tecnológica de Lima Sur"}
    return render(request, "saludo.html", diccionario)
 
def integrantes(request):
    integrantes = ["Casas Parisaca, Diego", "Fernandez Sotelo, Paolo Jeanpier", "Tomasto Hurtado, Johan Jesus"]
    diccionario = {"Titulo": "Lista de Integrantes",
                    "integrantes": integrantes}
 
    return render(request, "integrantes.html", diccionario)

def crear_producto(request):
    return render(request, "crear_producto.html")

def crear_curso(request):
    return render(request, "crear_curso.html")

