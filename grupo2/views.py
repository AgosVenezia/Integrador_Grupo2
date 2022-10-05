from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.urls import reverse

from django.template import loader

def index(request):
    if(request.method=='GET'):
        titulo = 'Titulo cuando se accede por GET - modificado'
    else:
        titulo = f'Titulo cuando accedo por otro metodo {request.method}'
    parameters_get = request.GET.get('otro')
    #return HttpResponse(f"""
        #<h1>{titulo}</h1>
        #<p>{parameters_get}</p>
    #""")
    listado_cursos = [
        {
            'nombre':'Fullstack Java',
            'descripcion':'Curso de Fullstack',
            'categoria':'Programación'
        },
        {
            'nombre':'Diseño UX/UI',
            'descripcion':'🎨',
            'categoria':'Diseño'
        },
        {
            'nombre':'Big Data',
            'descripcion':'test',
            'categoria':'Analisis de Datos'
        },
    ]

    return render(request,'grupo2/index.html',{
                                    'titulo_nombre':titulo,
                                    'cursos':listado_cursos,
                                    'parametros':parameters_get,
                                    'hoy': datetime.now})
    
def quienes_somos(request):
    #return redirect('saludar_por_defecto') #lleva a saludar o saludarbonito
    #return redirect(reverse('saludar', kwargs={'nombre':'Juliana'}))
    template = loader.get_template('grupo2/quienes_somos.html')
    context = {'titulo':'Codo a Codo - Quienes Somos'}
    return HttpResponse(template.render(context,request))

def ver_proyectos(request,anio=2022,mes=1):
    proyectos = []
    return render(request,'grupo2/proyectos.html',{'proyectos':proyectos})

def ver_cursos(request):
    listado_cursos = [
        {
            'nombre':'Fullstack Java',
            'descripcion':'Curso de Fullstack',
            'categoria':'Programación'
        },
        {
            'nombre':'Diseño UX/UI',
            'descripcion':'🎨',
            'categoria':'Diseño'
        },
        {
            'nombre':'Big Data',
            'descripcion':'test',
            'categoria':'Analisis de Datos'
        },
    ]

    return render(request,'grupo2/cursos.html',{'cursos':listado_cursos})
