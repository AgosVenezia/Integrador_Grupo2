from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.index,name="inicio"),
    path('quienessomos/',views.quienes_somos,name='quienes_somos'),
    path('eventos/',views.ver_eventos,name='eventos'),
    path('deportes/',views.ver_deportes,name='deportes'),
    path('administracion',views.index_administracion,name='inicio_administracion'),
]