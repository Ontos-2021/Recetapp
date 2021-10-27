from django.db import models


# Create your models here.

class Unidad(models.Model):
    nombre = models.CharField(max_length=45)
    abreviacion = models.CharField(max_length=7)

    def __str__(self):
        return self.nombre


class Tienda(models.Model):
    nombre = models.CharField(max_length=45)
    horario = models.CharField(max_length=70)

    def __str__(self):
        return self.nombre


class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)
    unidad = models.ForeignKey(Unidad, on_delete=models.DO_NOTHING)
    tienda = models.ManyToManyField(Tienda)

    def __str__(self):
        return self.nombre


class Receta(models.Model):
    nombre = models.CharField(max_length=50)
    tiempo = models.IntegerField
    vegano = models.BooleanField
    ingrediente = models.ManyToManyField(Ingrediente)
    cantidad = models.IntegerField

    def __str__(self):
        return self.nombre
