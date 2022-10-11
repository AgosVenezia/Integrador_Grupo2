from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.urls import reverse

from django.template import loader

def index(request):
    listado_cursos = [
        {
            'nombre':'Fullstack Java',
            'descripcion':'Curso de Fullstack',
            'categoria':'Programación'
        },
        {
            'nombre':'Diseño UX/IU',
            'descripcion':'🎨',
            'categoria':'Diseño'
        },
        {
            'nombre':'Big Data',
            'descripcion':'test',
            'categoria':'Analisis de Datos'
        },
    ]

    return render(request,'grupo2/publica/index.html',{'cursos':listado_cursos,})

def nuestro_club(request):
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
    contacto = []
    return render(request,'grupo2/publica/contacto.html',{'contacto':contacto})

def ver_actividades(request):
    listado_actividades = [
        {
            'nombre':'Fullstack Java',
            'descripcion':'Curso de Fullstack',
            'categoria':'Programación'
        },
        {
            'nombre':'Diseño UX/IU',
            'descripcion':'🎨',
            'categoria':'Diseño'
        },
        {
            'nombre':'Big Data',
            'descripcion':'test',
            'categoria':'Analisis de Datos'
        },
    ]
    return render(request,'grupo2/publica/actividades.html',{'cursos':listado_actividades})

def index_administracion(request):
    variable = 'test variable'
    return render(request, 'grupo2/administracion/index_administracion.html',{'variable':variable})