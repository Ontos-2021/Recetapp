from django.shortcuts import render
from Recetapp.Apps.Recetas.models import Receta


# Create your views here.

def index(request):

    return render(request, "index.html")


def recetas(request):

    recetas = Receta.objects.all()
    print(type(recetas))

    return render(request, "recetas.html", {"recetas": recetas})