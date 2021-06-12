from django.contrib import admin
from .models import Examen,Categoria,SubCategoria
# Register your models here.

admin.site.register(Examen)
admin.site.register(Categoria)
admin.site.register(SubCategoria)