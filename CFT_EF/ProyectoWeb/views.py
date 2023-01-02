from django.shortcuts import HttpResponse, redirect, render
from ProyectoWeb.models import Producto
from ProyectoWeb.forms import FormProducto
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
    if request.method == 'POST':
        formulario = FormProducto(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data

            codigo = data_form.get('codigo')
            nombre = data_form['nombre']
            precio_compra = data_form['precio_compra']
            precio_venta = data_form['precio_venta']
            fecha_compra = data_form['fecha_compra']
            estado = data_form['estado']

            producto = Producto(
                codigo = codigo,
                nombre = nombre,
                precio_compra = precio_compra,
                precio_venta = precio_venta,
                fecha_compra = fecha_compra,
                estado = estado
            )
            producto.save()
            # Crear Mensaje Flash
            messages.success(request, f'Se agregó correctamente el producto "{producto.nombre}"')

            return redirect('crear_producto')
    else:
        formulario = FormProducto()

    diccionario = {"Titulo": "Crear Producto Nuevo",
                    "form": formulario}

    return render(request, "crear_producto.html", diccionario)

def crear_curso(request):

    diccionario = {"Titulo": "Crear Curso Nuevo"}

    return render(request, "crear_curso.html", diccionario)

