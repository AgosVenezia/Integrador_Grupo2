from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.index,name="inicio"),
    path('quienessomos/',views.quienes_somos,name='quienes_somos'),
    path('proyectos/',views.ver_proyectos,name='proyectos'),
    path('cursos/',views.ver_cursos,name='cursos'),
]