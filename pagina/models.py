from django.db import models
# Create your models here.

class Alumno(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    edad = models.CharField(max_length=2)
    correo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=11)
    def __str__(self):
        return self.nombre

class Asignatura(models.Model):
    id_asig = models.CharField(max_length=3,primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    Alumno_rut = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    rut_prof = models.CharField(max_length=10,primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.CharField(max_length=2)
    correo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    Asignatura_id_asig = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombres

