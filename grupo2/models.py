from email.policy import default
from django.db import models

# Create your models here.


class Socio(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    apellido = models.CharField(max_length=100,verbose_name='Apellido')
    email = models.EmailField(max_length=150)
    dni = models.IntegerField(verbose_name='DNI')
    tipo_dni = models.CharField(max_length=10, default='dni')

class Persona(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')

    # esto me dice que en la clase que esta inmersa se comvierte en ABSTRACTA
    class Meta:
        abstract=True

class Vitalicio(Socio):
    fecha= models.DateField(("00/00/000"), auto_now=False, auto_now_add=False)


class Categoria(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    baja= models.BooleanField(default=0)

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    descripcion = models.TextField(null=True,verbose_name='Descripcion')
    #fecha_inicio = models.DateField(verbose_name='Fecha de Inicio')
    #portada = models.ImageField(upload_to='imagenes/',null=True,verbose_name='Portada')
    #many-to-one 
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    # socios una tabla intermedia
    socios = models.ManyToManyField(Socio) # crea la tabla muchos a muchos

class Inscripcion(models.Model):
    ESTADOS = [
        (1,'Inscripto'),
        (2,'Entrenando'),
        (3,'Finalizado'),
    ]
    fecha_creacion = models.DateField(verbose_name='Fecha de creacion')
    estudiante = models.ForeignKey(Socio, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    estado = models.IntegerField(choices=ESTADOS,default=1)

    def __str__(self):
        return self.id


# Herencia Multiple
#HERENCIA MULTIPLE
class PersonaM(models.Model):
    nombre_m = models.CharField(max_length=100,verbose_name='Nombre')
    apellido_m = models.CharField(max_length=150,verbose_name='Apellido')
    email_m = models.EmailField(max_length=150,null=True)
    dni_m = models.IntegerField(verbose_name="DNI")
    
    class Meta:
        abstract=True

class EstudianteM(PersonaM):
    matricula_m = models.CharField(max_length=10,verbose_name='Matricula')

class DocenteM(PersonaM):
    legajo_m = models.CharField(max_length=10,verbose_name='Legajo')
    