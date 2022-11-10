from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.index,name="inicio"),
    path('nuestroclub/',views.nuestro_club1,name='nuestro_club'),
    path('actividades/',views.ver_actividades,name='actividades'),
    path('horarios/',views.ver_horarios,name='horarios'),
    path('socios/',views.ver_socios,name='socios'),
    path('contacto/',views.ver_contacto,name='contacto'),
    path('administracion',views.index_administracion,name='inicio_administracion'),
    # modificado 08/11
    path('administracion/categorias', views.categorias_index,name='categorias_index'),
 #   path('api_proyectos/',views.api_proyectos,name="api_proyectos"),
 #   path('administracion/categorias/nuevo', views.categorias_nuevo,name='categorias_nuevo'),
]