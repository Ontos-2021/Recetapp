from django.shortcuts import render
from Recetapp.Apps.Recetas.models import Receta, RecetaIngrediente


# Create your views here.

def index(request):

    return render(request, "index.html")


def recetas(request):

    recetas = Receta.objects.all()

    return render(request, "recetas.html", {"recetas": recetas})