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

    def __str__(self):
        return self.nombre


class Receta(models.Model):
    nombre = models.CharField(max_length=50)
    tiempo = models.IntegerField(blank=True, null=True)
    vegano = models.BooleanField(null=True)

    def __str__(self):
        return self.nombre


class RecetIngrediente(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    cantidad = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "Receta: " + str(self.receta) + " | " + str(self.cantidad) + " " + str(self.ingrediente)


class TiendaIngredientes(models.Model):
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    precio = models.FloatField()
