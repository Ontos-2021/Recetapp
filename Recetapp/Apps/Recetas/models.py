from django.db import models


# Create your models here.

class Unidad(models.Model):
    nombre = models.CharField(max_length=45)
    abreviacion = models.CharField(max_length=7)


class Tienda(models.Model):
    nombre = models.CharField(max_length=45)
    horario = models.CharField(max_length=70)


class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)
    unidad = models.ForeignKey(Unidad)
    tienda = models.ManyToManyField(Tienda)


class Receta(models.Model):
    nombre = models.CharField(max_length=50)
    tiempo = models.IntegerField
    vegano = models.BooleanField
    ingrediente = models.ManyToManyField(Ingrediente)
