from django.db import models

# Create your models here.
from django.core.exceptions import ValidationError,ImproperlyConfigured
from django.core.validators import (
    MaxValueValidator, validate_comma_separated_integer_list,
)
from django.utils.translation import ugettext_lazy as _ 
from django.utils.timezone import now 
import random 
from django.contrib.auth.models import User


class CategoriaManager(models.Manager):
    def nueva_categoria(self,categoria):
        nueva_categoria = self.create(categoria=re.sub('\s+','-',categoria))
        nueva_categoria.save()
        return nueva_categoria
class Categoria(models.Model):
    categoria = models.CharField(verbose_name=_("Categoría"),max_length=250,blank=True,unique=True,null=True)
    objects = CategoriaManager()

    class Meta:
        verbose_name=_("Categría")
        verbose_name_plural=_("Categorias")
    def __str__(self):
        return self.categoria

class SubCategoria(models.Model):
    sub_categoria = models.CharField(verbose_name=_("Sub-Categoría"),max_length=250,blank=True, null=True)
    categoria = models.ForeignKey(Categoria, null=True, blank=True, verbose_name=_("Categoría"), on_delete=models.CASCADE)
    objects = CategoriaManager()

    class Meta:
        verbose_name=_("Sub-Categoría")
        verbose_name_plural=_("Sub-Categorias")
    def __str__(self):
        return self.sub_categoria+"("+self.categoria.categoria+")"

class Examen(models.Model):
    nombre = models.CharField(max_length=250)
    categoria = models.ForeignKey(Categoria, null=True, blank=True, verbose_name=_("Categoría"), on_delete= models.CASCADE)
    sub_categoria = models.ForeignKey(SubCategoria, null=True, blank=True, verbose_name=_("Sub-Categoría"), on_delete= models.CASCADE)
    numero_de_preguntas = models.IntegerField()
    tiempo = models.IntegerField(help_text="Duración del examen en minutos")
    puntuacion_para_pasar = models.IntegerField(help_text="Puntuación necesaria para aprobar")

    def __str__(self):
        return self.nombre+"("+self.categoria.categoria+" Tipo: "+self.sub_categoria.sub_categoria+")"
    def get_preguntas(self):
        preguntas = list(self.pregunta_set.all())
        random.shuffle(preguntas)
        return preguntas[:self.numero_de_preguntas]
    class Meta:
        verbose_name_plural=_("Examenes")
