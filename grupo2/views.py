from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.urls import reverse

from django.template import loader

from grupo2.forms import *

from django.contrib import messages # para responder los mensajes en pantalla

#--modificado 08/11
from grupo2.models import *
from grupo2.forms import *

#autenticacion
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required
from django.conf import settings

#para compartir los archivos estaticos
from django.views.static import serve 

def index(request):
    listado_entrenamientos=[]
    # si ingresa de post - 
    if(request.method == 'POST'):
        contacto_form = ContactoForm(request.POST) # se carga con los valores enviados
        # validar y guardar el comentario
        
    else:
        contacto_form = ContactoForm()  # se envia vacio va por GET

    return render(request,'grupo2/publica/index.html',{'cursos':listado_entrenamientos,'contacto_form':contacto_form})

def nuestro_club1(request):
    #return redirect('saludar_por_defecto')
    #return redirect(reverse('saludar', kwargs={'nombre':'Juliana'}))
    template = loader.get_template('grupo2/publica/nuestro_club.html')
    context = {'titulo':'Codo a Codo - Nuestro Club'}
    return HttpResponse(template.render(context,request))
    
def ver_horarios(request,anio=2022,mes=1):
    horarios = []
    return render(request,'grupo2/publica/horarios.html',{'horarios':horarios})

def ver_socios(request):
    socios = []
    return render(request,'grupo2/publica/socios.html',{'socios':socios})

def ver_contacto(request):
    listado_entrenamientos=[]
    # si ingresa de post - 
    if(request.method == 'POST'):
        contacto_form = ContactoForm(request.POST) # se carga con los valores enviados

        # validar y guardar el comentario
        if(contacto_form.is_valid()):
            # operacion con los datos ya validados
            # cargar en la sql
            messages.success(request,"Muchas gracias por comunicarte, en breve te estaremos contactando")
            contacto_form = ContactoForm()
        else:
            messages.warning(request,"Por favor, revisa los errores y vuelve a enviar")
    else:
        contacto_form = ContactoForm()  # se envia vacio va por GET

    return render(request,'grupo2/publica/contacto.html',
            {'cursos':listado_entrenamientos,'contacto_form':contacto_form})

def ver_actividades(request):
    listado_actividades = [
        {
            'nombre':'Fútbol',
            'descripcion':'Cebollitas',
            'categoria':'Deporte de equipo',
            'imagen':'/static/img/deporte_futbol_ninos.jpg'
        },
        {
            'nombre':'Atletismo',
            'descripcion':'Alta competencia',
            'categoria':'Individual',
            'imagen':'/static/img/atletismo.jpg'
        },
        {
            'nombre':'Básquet',
            'descripcion':'Adolescentes',
            'categoria':'Competencia',
            'imagen':'/static/img/deporte_basket.jpg'
        },
        {
            'nombre':'Musculación',
            'descripcion':'Personalizado',
            'categoria':'Competencia',
            'imagen':"/static/img/deporte_musculacion.jpg"
        }]
    return render(request,'grupo2/publica/actividades2.html',{'cursos':listado_actividades})

def index_administracion(request):
    variable = 'test variable'
    return render(request, 'grupo2/administracion/index_administracion.html',{'variable':variable})

# ---------------------------------------------------------------------------
# ACTIVIDADES
def ver_actividade2(request):
    cursos = Curso.objects.filter(baja=False)
     
    return render(request,'grupo2/publica/actividades.html',{'cursos':cursos})




# ----------------------------------------------------------------------------
#  ***  ADMINITRACION   ***
#----------------------------------------------------------------------------------
# CATEGORIAS  de Entrenamientos

def categorias_index(request):
    # queryset

    # muestra todo lo que tiene
    #categorias = Categoria.objects.all()

    # SOlo muestra los que estan activos BAJA = False
    categorias = Categoria.objects.filter(baja=False)

    return render(request,'grupo2/administracion/categorias/index.html',{'categorias':categorias})

def categorias_nuevo(request):
    if(request.method=='POST'):
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid():
            nombre2 = formulario.cleaned_data['nombre']
            nueva_categoria = Categoria(nombre=nombre2)
            nueva_categoria.save()
            return redirect('categoria_index')
    else:
        formulario = CategoriaForm()
    return render(request,'grupo2/administracion/categorias/nuevo.html',{'formulario':formulario})

def categorias_editar(request,id):

    try:
        edito = Categoria.objects.get(pk=id)
    except Categoria.DoesNotExist:
        return render(request,'grupo2/administracion/404_admin.html')
    
    if(request.method =='POST'):
        formulario = CategoriaForm(request.POST, instance=edito)
        if formulario.is_valid():
            formulario.save() 
            return redirect('categoria_index')
    else:
        
        formulario = CategoriaForm(instance=edito)
    return render(request,'grupo2/administracion/categorias/editar.html',{'formulario':formulario})

def categorias_eliminar(request,id):
    try:
        categoria = Categoria.objects.get(pk=id) # evito que se intente borrar algo que no existe
    except Categoria.DoesNotExist:
        return render(request,'grupo2/administracion/404_admin.html')
    categoria.soft_delete()
    return redirect('categoria_index')

#-----------------------------------------
# CIUDADES de residencia d elos Socios

def ciudades_index(request):
    # muestra todo lo que tiene
    #ciudades = ciudadResidencia.objects.all()

    # SOlo muestra los que estan activos BAJA = False
    ciudades = CiudadResidencia.objects.filter(baja=False)

    return render(request,'grupo2/administracion/ciudad/index.html',{'ciudades':ciudades})

def ciudades_nuevo(request):
    if(request.method=='POST'):
        formulario = CiudadForm(request.POST)
        if formulario.is_valid():
            # esto me devuelve un diccionario de los campos cargados en el formularios nuevo
            dic = formulario.cleaned_data 
            nueva= CiudadResidencia(ciudad=dic['ciudad'],provincia=dic['provincia'],codigoPostal=dic['codigoPostal'])
            
            nueva.save()
            return redirect('ciudad_index')
    else:
        formulario = CiudadForm()
    return render(request,'grupo2/administracion/ciudad/nuevo.html',{'formulario':formulario})

def ciudades_editar(request,id):
    try:
        edito = CiudadResidencia.objects.get(pk=id)
    except CiudadResidencia.DoesNotExist:
        return render(request,'grupo2/administracion/404_admin.html')
    
    if(request.method =='POST'):
        formulario = CiudadForm(request.POST, instance=edito)
        if formulario.is_valid():
            formulario.save() 
            return redirect('ciudad_index')
    else:
        
        formulario = CiudadForm(instance=edito)
    return render(request,'grupo2/administracion/ciudad/editar.html',{'formulario':formulario})

def ciudades_eliminar(request,id):
    try:
        borra = CiudadResidencia.objects.get(pk=id) # evito que se intente borrar algo que no existe
        
    except CiudadResidencia.DoesNotExist:
        return render(request,'grupo2/administracion/404_admin.html')
    borra.soft_delete()
    return redirect('ciudad_index')
 
#------------------------------------------------------
# COMPROBANTES de pago de Socios

def comprobantes_index(request):
    #comprobantes = Comprobante.objects.filter(baja=False)
    comprobantes = Comprobante.objects.filter(baja=False)

    return render(request,'grupo2/administracion/comprobante/index.html',{'comprobantes':comprobantes})

def comprobantes_nuevo(request):
    if(request.method=='POST'):
        formulario = ComprobanteForm(request.POST)
        if formulario.is_valid():
            dic = formulario.cleaned_data
            nueva= Comprobante( comprobante=dic['comprobante'],fecha=dic['fecha'],montoComprobante=dic['montoComprobante'],observaciones=dic['observaciones'])
            
           
            nueva.save()
            return redirect('comprobante_index')
    else:
        formulario = ComprobanteForm()
    return render(request,'grupo2/administracion/comprobante/nuevo.html',{'formulario':formulario})

def comprobantes_editar(request,id):
    try:
        edito = Comprobante.objects.get(pk=id)
    except Comprobante.DoesNotExist:
        return render(request,'grupo2/administracion/404_admin.html')
    
    if(request.method =='POST'):
        formulario = ComprobanteForm(request.POST, instance=edito)
        if formulario.is_valid():
            formulario.save() 
            return redirect('comprobante_index')
    else:
        
        formulario = ComprobanteForm(instance=edito)
    return render(request,'grupo2/administracion/comprobante/editar.html',{'formulario':formulario})

def comprobantes_eliminar(request,id):
    try:
        borra = Comprobante.objects.get(pk=id) # evito que se intente borrar algo que no existe
    except Comprobante.DoesNotExist:
        return render(request,'grupo2/administracion/404_admin.html')
    borra.soft_delete()
    return redirect('comprobante_index')

#------------------------------------------------------
# CUOTAS de los socios

def cuotas_index(request):
    cuotas = Cuota.objects.filter(baja=False)

    return render(request,'grupo2/administracion/cuota/index.html',{'cuotas':cuotas})

def cuotas_nuevo(request):
    if(request.method=='POST'):
        formulario = CuotaForm(request.POST)
        if formulario.is_valid():
            dic = formulario.cleaned_data
            nueva= Cuota( cuota=dic['cuota'],socio=dic['socio'],comprobante=dic['comprobante'],montoCuota=dic['montoCuota'])
            
           
            nueva.save()
            return redirect('cuota_index')
    else:
        formulario = CuotaForm()
    return render(request,'grupo2/administracion/cuota/nuevo.html',{'formulario':formulario})

def cuotas_editar(request,id):
    try:
        edito = Cuota.objects.get(pk=id)
    except Cuota.DoesNotExist:
        return render(request,'grupo2/administracion/404_admin.html')
    
    if(request.method =='POST'):
        formulario = CuotaForm(request.POST, instance=edito)
        if formulario.is_valid():
            formulario.save() 
            return redirect('cuota_index')
    else:
        
        formulario = CuotaForm(instance=edito)
    return render(request,'grupo2/administracion/comprobante/editar.html',{'formulario':formulario})

def cuotas_eliminar(request,id):
    try:
        borra = Cuota.objects.get(pk=id) # evito que se intente borrar algo que no existe
    except Cuota.DoesNotExist:
        return render(request,'grupo2/administracion/404_admin.html')
    borra.soft_delete()
    return redirect('cuota_index')

#-------------------------------------------------------------------
# CURSOS dictados por el CLUB

def cursos_index(request):
    cursos = Curso.objects.all()
     
    return render(request,'grupo2/administracion/curso/index.html',{'cursos':cursos})

def cursos_nuevo(request):
    if(request.method=='POST'):
        formulario = CursoForm(request.POST)
        if formulario.is_valid():
            dic = formulario.cleaned_data
            nueva= Curso( nombre=dic['nombre'],descripcion=dic['descripcion'],imagen=dic['imagen'],categoria=dic['categoria'],dia=dic['dia'],turno=dic['turno'])
            
            nueva.save()
            return redirect('curso_index')
    else:
        formulario = CursoForm()
    return render(request,'grupo2/administracion/curso/nuevo.html',{'formulario':formulario})

def cursos_editar(request,id):
    try:
        edito = Curso.objects.get(pk=id)
    except Curso.DoesNotExist:
        return render(request,'grupo2/administracion/404_admin.html')
    
    if(request.method =='POST'):
        formulario = Curso(request.POST, instance=edito)
        if formulario.is_valid():
            formulario.save() 
            return redirect('curso_index')
    else:
        
        formulario = CursoForm(instance=edito)
    return render(request,'grupo2/administracion/curso/editar.html',{'formulario':formulario})

def cursos_eliminar(request,id_socio):
    try:
        borra = Curso.objects.get(pk=id_socio) # evito que se intente borrar algo que no existe
    except Curso.DoesNotExist:
        return render(request,'grupo2/administracion/404_admin.html')
    borra.soft_delete()
    return redirect('curso_index')

#-------------------------------------------------------------------
# SOCIOS

def socios_index(request):
    # muestra todo lo que tiene
    socios = Socio.objects.all()

    # SOlo muestra los que estan activos BAJA = False
    #categorias = Categoria.objects.filter(baja=False)

    return render(request,'grupo2/administracion/socio/index.html',{'socios':socios})

def socios_nuevo(request):
    if(request.method=='POST'):
        formulario = SocioForm(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data
            nueva= Socio(nombre=nombre)
            nueva.save()
            return redirect('socio_index')
    else:
        formulario = SocioForm()
    return render(request,'grupo2/administracion/socio/nuevo.html',{'formulario':formulario})

def socios_editar(request,id):
    try:
        edito = Socio.objects.get(pk=id)
    except Socio.DoesNotExist:
        return render(request,'grupo2/administracion/404_admin.html')
    
    if(request.method =='POST'):
        formulario = Socio(request.POST, instance=edito)
        if formulario.is_valid():
            formulario.save() 
            return redirect('socio_index')
    else:
        formulario = SocioForm(instance=edito)
    return render(request,'grupo2/administracion/socio/editar.html',{'formulario':formulario})

def socios_eliminar(request,id):
    try:
        borra = Socio.objects.get(pk=id) # evito que se intente borrar algo que no existe
    except Socio.DoesNotExist:
        return render(request,'grupo2/administracion/404_admin.html')
    borra.soft_delete()
    return redirect('socio_index')












    """
AUTENTICACION
"""

#--------------------------------------------------------------------





def grupo2_login(request):
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' Bienvenido/a {username} !!')
            return redirect('inicio')
        else:
            messages.error(request, f'Cuenta o contraseña incorrecta, realice el login correctamente')
    form = AuthenticationForm()
    return render(request, 'grupo2/publica/login.html', {'form': form, 'title': 'Log in'})


def grupo2_registrarse(request):
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Tu cuenta fue creada con éxito! Ya te podes loguear en el sistema.')
            return redirect('login')
    else:
        form = RegistrarUsuarioForm()
    return render(request, 'grupo2/publica/registrarse.html', {'form': form})


def iniciosecion(request):
    listado_entrenamientos=[]
    # si ingresa de post - 
    if(request.method == 'POST'):
        contacto_form = ContactoForm(request.POST) # se carga con los valores enviados
        # validar y guardar el comentario
        
    else:
        contacto_form = ContactoForm()  # se envia vacio va por GET

    return render(request,'grupo2/publica/iniciosecion.html',{'cursos':listado_entrenamientos,'contacto_form':contacto_form})


# ----------------------------------------
# AUTENTICACION

# 29/11   - Usuarios
@login_required(login_url=settings.LOGIN_URL) # protege que solo este logueado para accdeder
def index_administracion(request):
    variable = 'test variable'
    return render(request,'grupo2/administracion/index_administracion.html',{'variable':variable})

def grupo2_login(request):
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:

            #registra el usuario en la sesion
            form = login(request, user)
            nxt = request.GET.get("next",None)
            messages.success(request, f' Ultimo inicio fue de {username} !!')
            if nxt is None:
                return redirect('inicio')
            else:
                return redirect(nxt)
        else:
            messages.error(request, f'Cuenta o password incorrecto, realice el inicio de sesión correctamente')
    form = AuthenticationForm()
    return render(request, 'grupo2/publica/login.html', {'form': form})


# --------------------------------------------
# cambio de contraseña

from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):

    form_class = CambiarContraseniaForm
    template_name = 'cambiar_contrasenia.html'

#-------------------------------------------------------