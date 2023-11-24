from django.db import models

class Operacion(models.Model):
    operacion = models.CharField(max_length=255)
    resultado = models.FloatField()