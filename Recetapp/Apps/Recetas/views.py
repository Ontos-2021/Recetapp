from django.shortcuts import render
from Recetapp.Apps.Recetas.models import Receta


# Create your views here.

def index(request):

    recetas = Receta.objects.all()

    return render(request, "index.html", {"recetas": recetas})
