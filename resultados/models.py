from django.db import models
from examenes.models import Examen
from django.contrib.auth.models import User 
from datetime import datetime, time
from django.utils import timezone

# Create your models here.

class Resultado(models.Model):
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nota = models.FloatField()
    fecha = models.DateTimeField(default=timezone.now(),blank=True)
    def __str__(self):
        return str(self.pk)
