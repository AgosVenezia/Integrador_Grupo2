from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.urls import reverse

from django.template import loader

from grupo2.form import *

from django.contrib import messages # para responder los mensajes en pantalla


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
            'imagen':'/static/img/Atletismo.jpg'
        },
        {
            'nombre':'Basquet',
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
    return render(request,'grupo2/publica/actividades.html',{'cursos':listado_actividades})

def index_administracion(request):
    variable = 'test variable'
    return render(request, 'grupo2/administracion/index_administracion.html',{'variable':variable})