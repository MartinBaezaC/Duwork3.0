from django.contrib import admin
from .models import Alumno,Asignatura,Profesor
# Register your models here.

admin.site.register(Alumno)
admin.site.register(Asignatura)
admin.site.register(Profesor)
