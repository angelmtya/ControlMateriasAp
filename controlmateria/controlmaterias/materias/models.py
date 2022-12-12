from django.db import models

# Create your models here.

class Materia(models.Model):
    siglas = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=8, null=True)
    
    def __str__(self):
       return self.nombre
    
class Alumno(models.Model):
    matricula = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=100, null=True)
    primer_apellido = models.CharField(max_length=100, null=True)
    segundo_apellido = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.nombre


# class Aprobada(models.Model):
#     matricula = models.ForeignKey('materias.Alumno', on_delete=models.CASCADE )

class Tiempo(models.Model):
    fecha_inicio = models.DateField(('Fecha de inicio'), auto_now=False, auto_now_add=False, null=True, blank=True)
    fecha_final = models.DateField(('Fecha de finalización'), auto_now=False, auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.fecha_inicio
    
    
class DirectorioModel(models.Model):
    carpeta = models.FileField()