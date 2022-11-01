from email.policy import default
from django.db import models

# Create your models here.


class Socio(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    apellido = models.CharField(max_length=100,verbose_name='Apellido')
    email = models.EmailField(max_length=150)
    dni = models.IntegerField(verbose_name='DNI')
    tipo_dni = models.CharField(max_length=10, default='dni')


class Categoria(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    baja= models.BooleanField(default=0)

    def __str__(self):
        return self.nombre