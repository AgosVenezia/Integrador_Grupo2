from email.policy import default
from django.db import models
from .choices import *

# Create your models here.

class ciudadResidencia (models.Model):  
    idCiudad=models.IntegerField(max_length=3)
    ciudad=models.CharField(max_length=100,verbose_name='Ciudad')
    provincia=models.CharField(max_length=100,verbose_name='Provincia')
    codigoPostal=models.IntegerField(max_length=4,verbose_name='Codigo Postal')

class Socio(models.Model):
    idSocio=models.IntegerField(max_length=4,primary_key=True,default=0000) # numero interno de referencia - PK
    fechaAsociacion= models.DateField(verbose_name='Fecha de alta en al club',null=True) # fecha que ingreso al club
    idCategoriaSocio=models.CharField(max_length=1, choices=categoriaSocio, default='A')  # Categoria de socio 0: 2:vitalicio 
    distintiva=models.CharField(max_length=6,null=True) # Distintiva propia segun un convenio internacional
    categoriaDistintiva=models.CharField(max_length=1, choices=categoriaDistintiva, default='N') # Categoria que corresponde a su distintiva
    expediente = models.FileField(upload_to='expedientes/', null=True ) # archivo de referencia con contrado y seguro
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    apellido = models.CharField(max_length=100,verbose_name='Apellido')
    estadoCivil=models.CharField(max_length=1, choices=estadoCivil, default='S')
    sexo=models.CharField(max_length=1,choices=sexos, default='F') # M, F, N, 0,
    tipo_dni = models.CharField(max_length=10, default='DNI')
    dni = models.IntegerField(verbose_name='DNI',null=True)
    cuil = models.IntegerField(max_length=11,null=True)
    fechaNacimient = models.DateField(verbose_name='Fecha de nacimiento',null=True)
    direccion = models.CharField(max_length=100,verbose_name='direccion',null=True)
    ciudadResidencia=models.ForeignKey(ciudadResidencia, on_delete=models.CASCADE, null=True)
    ocupacion=models.CharField(max_length=100,verbose_name='Ocupacion',null=True)
    telDomicilio=models.IntegerField(max_length=15,null=True)
    telCelular=models.IntegerField(max_length=15,null=True)
    email = models.EmailField(max_length=150,null=True)
    condicionDePago=models.CharField(max_length=1, choices=condicionDePago, default='S') # 0:en sede  1:pasa cobrador por le domicilio
    pesentadoPor=models.IntegerField(max_length=4,null=True) # que socio lo presento
    venciDistintiva=models.DateField(verbose_name='Vencimiento de la Distintiva',null=True)  # Vencimiento de la Distintiva

    web=models.CharField(max_length=100,verbose_name='web',null=True)

    
class comprobante (models.Model): 
    comprobante=models.IntegerField(max_length=8,primary_key=True)  # numero de comprobante en la factura
    fecha= models.DateField(null=True) # fecha de pago
    montoComprobante=models.FloatField(max_length=6,default=0,verbose_name='Monto Total')  # monto total del comprobante
    observaciones=models.CharField(max_length=100,verbose_name='Observacion',null=True)  # opcional



class cuota (models.Model):  
    cuota=models.IntegerField(max_length=6,primary_key=True)  # numero de cuota  año+mes ej: 202003
    socio=models.ForeignKey(Socio, on_delete=models.CASCADE, null=True)  # referencia con tabla socio a quien corresponde la cuota
    comprobante=models.ForeignKey(comprobante, on_delete=models.CASCADE,null=True)  # referencia con el comprobante donde se abono la cuota
    montoCuota=models.FloatField(max_length=6,default=0)  # monto de la cuota que se abono



    



      
    
    



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
    imagen= models.FileField(upload_to='../static/img/', null=True )
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
    