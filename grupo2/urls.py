from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.index,name="inicio"),
    path('nuestroclub/',views.nuestro_club,name='nuestro_club'),
    path('actividades/',views.ver_actividades,name='actividades'),
    path('horarios/',views.ver_horarios,name='horarios'),
    path('socios/',views.ver_socios,name='socios'),
    path('contacto/',views.ver_contacto,name='contacto'),
    path('administracion',views.index_administracion,name='inicio_administracion'),
]