from email.policy import default
from django.db import models
from .choices import *

# Create your models here.

class CiudadResidencia (models.Model):  
#    idCiudad=models.IntegerField(primary_key=True,verbose_name='Identificacion de Ciudad')
    ciudad=models.CharField(max_length=100,verbose_name='Ciudad')
    provincia=models.CharField(max_length=100,verbose_name='Provincia')
    codigoPostal=models.CharField(max_length=8,verbose_name='Codigo Postal')
    baja= models.BooleanField(default=0)
    def __str__(self):
        return self.ciudad

    # esto es par categoria delete
    def soft_delete(self):
        self.baja=True  #modifica el estado
        super().save()

    def restore(self):
        self.baja=False # es para activarlo
        super().save()

    # estor muestra la palabra en plural  en el formulario
    class Meta():
        verbose_name_plural = 'Ciudades'

class Socio(models.Model):
    id=models.IntegerField(verbose_name='Numero de Socio',primary_key=True,default=0000) # numero interno de referencia - PK
    fechaAsociacion= models.DateField(verbose_name='Fecha de alta en al club',null=True) # fecha que ingreso al club
    idCategoriaSocio=models.CharField(verbose_name='Categoria de Socio ante el Club',max_length=1, choices=categoriaSocio, default='A')  # Categoria de socio 0: 2:vitalicio 
    distintiva=models.CharField(verbose_name='Señal Distintiva',max_length=6,null=True) # Distintiva propia segun un convenio internacional
    categoriaDistintiva=models.CharField(verbose_name='Categoria de señal Distintiva',max_length=1, choices=categoriaDistintiva, default='N') # Categoria que corresponde a su distintiva
    #expediente = models.FileField(verbose_name='Carpeta de expedientes',upload_to='expedientes/', null=True ) # archivo de referencia con contrado y seguro
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    apellido = models.CharField(max_length=100,verbose_name='Apellido')
    estadoCivil=models.CharField(max_length=1, choices=estadoCivil, default='S',verbose_name='Estado Civil')
    sexo=models.CharField(verbose_name='Sexo',max_length=1,choices=sexos, default='F') # M, F, N, 0,
    tipo_dni = models.CharField(verbose_name='Tipo de Documento',max_length=10, default='DNI')
    dni = models.IntegerField(verbose_name='Numero de Documento',null=True)
    cuil = models.IntegerField(verbose_name='CUIL O CUIT',null=True)
    fechaNacimient = models.DateField(verbose_name='Fecha de nacimiento',null=True)
    direccion = models.CharField(max_length=100,verbose_name='Direccion',null=True)
    ciudadResidencia=models.ForeignKey(CiudadResidencia, on_delete=models.CASCADE, null=True,verbose_name='Ciudad')
    ocupacion=models.CharField(max_length=100,verbose_name='Ocupacion',null=True)
    telDomicilio=models.IntegerField(verbose_name='Teléfono Fijo',null=True)
    telCelular=models.IntegerField(verbose_name='Teléfono Celular',null=True)
    email = models.EmailField(verbose_name='Correo Electrónico - email',max_length=150,null=True)
    condicionDePago=models.CharField(verbose_name='Condicion de Pago',max_length=1, choices=condicionDePago, default='S') # 0:en sede  1:pasa cobrador por le domicilio
    pesentadoPor=models.IntegerField(verbose_name='Fue presentado por',null=True) # que socio lo presento
    venciDistintiva=models.DateField(verbose_name='Vencimiento de la Distintiva',null=True)  # Vencimiento de la Distintiva

    web=models.CharField(max_length=100,verbose_name='web',null=True)
    baja= models.BooleanField(default=1)

    # metodo str permite que sea los que se muestre como referencia en el admin
    def __str__(self):
        return self.distintiva

    # esto es par categoria delete
    def soft_delete(self):
        self.baja=True  #modifica el estado
        super().save()

    def restore(self):
        self.baja=False # es para activarlo
        super().save()

    class Meta():
        verbose_name_plural = 'Socios'
    
class Comprobante (models.Model): 
    comprobante=models.CharField(max_length=6,verbose_name='Numero de Comprobante',null=True)  # numero de comprobante en la factura
    fecha= models.DateField(null=True,verbose_name='Fecha MM/DD/AAAA') # fecha de pago
    montoComprobante=models.FloatField(default=0,verbose_name='Monto Total')  # monto total del comprobante
    observaciones=models.CharField(max_length=100,verbose_name='Observación',blank=True,null=True)  # opcional
    baja= models.BooleanField(default=1)
    
    def __str__(self):
        return self.comprobante

    # esto es par categoria delete
    def soft_delete(self):
        self.baja=True  #modifica el estado
        super().save()

    def restore(self):
        self.baja=False # es para activarlo
        super().save()

    # estor muestra la palabra en plural 
    class Meta():
        verbose_name_plural = 'Comprobantes'

class Cuota (models.Model):  
    cuota=models.CharField(max_length=6,null=True)  # numero de cuota  año+mes ej: 202003
    socio=models.ForeignKey(Socio, on_delete=models.CASCADE, null=True)  # referencia con tabla socio a quien corresponde la cuota
    comprobante=models.ForeignKey(Comprobante, on_delete=models.CASCADE,null=True)  # referencia con el comprobante donde se abono la cuota
    montoCuota=models.FloatField(max_length=6,default=0)  # monto de la cuota que se abono
    baja= models.BooleanField(default=1)
    
    def __str__(self):
        return self.cuota

    # esto es par categoria delete
    def soft_delete(self):
        self.baja=True  #modifica el estado
        super().save()

    def restore(self):
        self.baja=False # es para activarlo
        super().save()
    
    class Meta():
        verbose_name_plural = 'Cuotas'

class Categoria(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    baja= models.BooleanField(default=1)
    
    def __str__(self):
        return self.nombre

    # esto es par categoria delete
    def soft_delete(self):
        self.baja=True  #modifica el estado
        super().save()

    def restore(self):
        self.baja=False # es para activarlo
        super().save()

    class Meta():
        verbose_name_plural = 'Categorias'

class Curso(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    descripcion = models.TextField(null=True,verbose_name='Descripcion')
    imagen= models.FileField(verbose_name='Imagen a mostrar',upload_to='imagen_curso/', null=True )
    #fecha_inicio = models.DateField(verbose_name='Fecha de Inicio')
    #portada = models.ImageField(upload_to='imagenes/',null=True,verbose_name='Portada')
    #many-to-one 
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    # socios una tabla intermedia
    #socios = models.ManyToManyField(Socio) # crea la tabla muchos a muchos
    dia =models.CharField(verbose_name='Dias',max_length=1, choices=dias, default='1') 
    turno = models.CharField(verbose_name='Turno',max_length=1, choices=turnos, default='1') 
    baja= models.BooleanField(default=1)
    
    def __str__(self):
        return self.nombre

    # esto es par categoria delete
    def soft_delete(self):
        self.baja=True  #modifica el estado
        super().save()

    def restore(self):
        self.baja=False # es para activarlo
        super().save()
    
    class Meta():
        verbose_name_plural = 'Cursos'
      
      

# modelo abstracto

class Persona(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')

    # esto me dice que en la clase que esta inmersa se comvierte en ABSTRACTA
    class Meta:
        abstract=True


class Inscripcion(models.Model):
    
    fecha_creacion = models.DateField(verbose_name='Fecha de creacion')
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE,verbose_name='Socio')
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE,verbose_name='Curso')
    estado = models.IntegerField(choices=ESTADOS,default=1,verbose_name='Estado de la Inscripción')

    def __str__(self):
        return self.id

# esto que sigue no se esta utilizando solo esta como referencia de las clases

#HERENCIA MULTIPLE
class PersonaM(models.Model):
    nombre_m = models.CharField(max_length=100,verbose_name='Nombre')
    apellido_m = models.CharField(max_length=150,verbose_name='Apellido')
    email_m = models.EmailField(max_length=150,null=True)
    dni_m = models.IntegerField(verbose_name="DNI")
    
    # al ser abstracta no se genera la tabla PersonaM en el sql
    # y genera estos campos en las herencias
    class Meta:
        abstract=True

class EstudianteM(PersonaM):
    matricula_m = models.CharField(max_length=10,verbose_name='Matricula')

class DocenteM(PersonaM):
    legajo_m = models.CharField(max_length=10,verbose_name='Legajo')
    