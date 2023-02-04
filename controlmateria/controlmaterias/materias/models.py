from django.db import models

# Create your models here.

class Materia(models.Model):
    clave = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=100, null=True)
    
    def __str__(self):
       return self.clave
    
class Alumno(models.Model):
    matricula = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.matricula


class Aprobada(models.Model):
    id_aprobada= models.AutoField(primary_key=True)
    matricula_alumno = models.ForeignKey(Alumno, null=True, blank=True, on_delete=models.CASCADE)
    materia_ap = models.ForeignKey(Materia, null=True, blank=True, on_delete=models.CASCADE)

# class Fecha(models.Model):
#     fecha_inicio = models.DateField(('Fecha de inicio'), auto_now=False, auto_now_add=False, null=True, blank=True)
#     fecha_final = models.DateField(('Fecha de finalización'), auto_now=False, auto_now_add=False, null=True, blank=True)

#     def __str__(self):
#         return self.fecha_inicio
    
    
class DirectorioModel(models.Model):
     carpeta = models.FileField()
    
    