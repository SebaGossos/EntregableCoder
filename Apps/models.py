from django.db import models

class Familiares(models.Model):
    Nombre = models.CharField(max_length=25)
    Apellido = models.CharField(max_length=30)
    Año_de_nacimiento = models.IntegerField()
    Email = models.EmailField()
    Fecha_actual = models.DateField()


