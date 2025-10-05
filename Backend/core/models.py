# core/models.py
from django.db import models

class Clima(models.Model):
    id = models.AutoField(primary_key=True) 
    dia = models.IntegerField(blank=True, null=True)
    temperatura = models.IntegerField(blank=True, null=True)
    indice_uv = models.IntegerField(blank=True, null=True)
    precipitacion = models.FloatField(blank=True, null=True) 
    velocidad_aire = models.FloatField(blank=True, null=True)
    pais = models.TextField(blank=True, null=True)
    ciudad = models.TextField(blank=True, null=True)
    sensacion_termica = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clima'