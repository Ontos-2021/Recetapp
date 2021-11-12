from django.shortcuts import render, redirect
from Recetapp.Apps.Recetas.models import Receta, RecetaIngrediente


# Create your views here.

def index(request):

    return render(request, "index.html")


def recetas(request):

    recetas = Receta.objects.all()

    return render(request, "recetas.html", {"recetas": recetas})


def crear_receta(request):
    

    return render(request, "crear_receta.html")


def guardar_receta(request):

    if request.method == "POST":

        nombre = request.POST["nombre"]
        tiempo = request.POST["tiempo"]
        # vegano = request.POST["vegano"]
        descripcion = request.POST["descripcion"]

        print(f"Nombre: {nombre}")
        print(f"Tiempo: {tiempo}")
        print(f"Vegano: {vegano}")
        print(f"Descripcion: {descripcion}")

        receta = Receta(
            nombre = nombre,
            tiempo = tiempo,
            # vegano = vegano,
            descripcion = descripcion
        )

        receta.save()
    
    redirect('recetas:recetas')

