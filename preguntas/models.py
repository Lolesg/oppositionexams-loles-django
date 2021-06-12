from django.db import models

# Create your models here.

from examenes.models import Examen,Categoria,SubCategoria

class Pregunta(models.Model):
    texto = models.CharField(max_length=2500)
    imagen = models.ImageField(upload_to='media/',null=True,blank=True)
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE)
    crear = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.texto)
    def get_respuestas(self):
        return self.respuesta_set.all()
class Respuesta(models.Model):
    respuesta = models.CharField(max_length=2500)
    correcta = models.BooleanField(default=False)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    crear = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"pregunta: {self.pregunta.texto},imagen: {self.pregunta.imagen},respuesta: {self.respuesta},  correcta: {self.correcta}"