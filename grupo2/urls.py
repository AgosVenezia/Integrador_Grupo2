from django.urls import path, re_path, include
from . import views
from django.contrib.auth import views as auth_views


# Achivos media
from django.conf.urls.static import static
from django.conf import settings,urls



urlpatterns = [
    path('',views.index,name="inicio"),
    path('nuestroclub/',views.nuestro_club1,name='nuestro_club'),
    path('actividades/',views.ver_actividade2,name='actividades'),
    path('actividades2/',views.ver_actividades,name='actividades2'),
    path('horarios/',views.ver_horarios,name='horarios'),
    path('socios/',views.ver_socios,name='socios'),
    path('contacto/',views.ver_contacto,name='contacto'),

    path('administracion',views.index_administracion,name='inicio_administracion'),

    
    

# Categorias de los entrenamientos
    # modificado 08/11
    path('administracion/categorias', views.categorias_index,name='categoria_index'),
#   path('api_proyectos/',views.api_proyectos,name="api_proyectos"),

    path('administracion/categorias/nuevo', views.categorias_nuevo,name='categoria_nuevo'),
    path('administracion/categorias/editar/<int:id>', views.categorias_editar,name='categoria_editar'),
    path('administracion/categorias/eliminar/<int:id>', views.categorias_eliminar,name='categoria_eliminar'),

# Ciudad
    path('administracion/ciudad', views.ciudades_index,name='ciudad_index'),
    path('administracion/ciudad/nuevo', views.ciudades_nuevo,name='ciudad_nuevo'),
    path('administracion/ciudad/editar/<int:id>', views.ciudades_editar,name='ciudad_editar'),
    path('administracion/ciudad/eliminar/<int:id>', views.ciudades_eliminar,name='ciudad_eliminar'),

# Comprobante
    path('administracion/comprobante', views.comprobantes_index,name='comprobante_index'),
    path('administracion/comprobante/nuevo', views.comprobantes_nuevo,name='comprobante_nuevo'),
    path('administracion/comprobante/editar/<int:id>', views.comprobantes_editar,name='comprobante_editar'),
    path('administracion/comprobante/eliminar/<int:id>', views.comprobantes_eliminar,name='comprobante_eliminar'),


# Socios
    path('administracion/socio', views.socios_index,name='socio_index'),
    path('administracion/socio/nuevo', views.socios_nuevo,name='socio_nuevo'),
    path('administracion/socio/editar/<int:id>', views.socios_editar,name='socio_editar'),
    path('administracion/socio/eliminar/<int:id>', views.socios_eliminar,name='socio_eliminar'),



# Cuota
    path('administracion/cuota', views.cuotas_index,name='cuota_index'),
    path('administracion/cuota/nuevo', views.cuotas_nuevo,name='cuota_nuevo'),
    path('administracion/cuota/editar/<int:id>', views.cuotas_editar,name='cuota_editar'),
    path('administracion/cuota/eliminar/<int:id>', views.cuotas_eliminar,name='cuota_eliminar'),


# Curso
    path('administracion/curso', views.cursos_index,name='curso_index'),
    path('administracion/curso/nuevo', views.cursos_nuevo,name='curso_nuevo'),
    path('administracion/curso/editar/<int:id>', views.cursos_editar,name='curso_editar'),
    path('administracion/curso/eliminar/<int:id>', views.cursos_eliminar,name='curso_eliminar'),

#-------------------------------
#  CUENTAS

    # path('cuentas/login/', views.cac_login,name='login'),
    # path('cuentas/logout/',
    #  auth_views.LogoutView.as_view(template_name='cac/publica/index.html'), name='logout'),
    path('cuentas/registrarse', views.grupo2_registrarse, name='registrarse'),
    
    path('account/login/',auth_views.LoginView.as_view(template_name='grupo2/publica/login.html')),
		# path('account/logout/',
    #      auth_views.LogoutView.as_view(template_name='cac/publica/logout.html'), name='logout'),
  	path('account/password_change/',auth_views.PasswordChangeView.as_view(success_url='/')),
    path('account/',include('django.contrib.auth.urls')),

#Autenticacion
    path('cuentas/login', views.grupo2_login,name='login'),
    path('cuentas/logout/',
         auth_views.LogoutView.as_view(template_name='grupo2/publica/index.html'), name='logout'),

    path('iniciosecion/',views.iniciosecion,name='inicio2'),
 ] + static(settings.MEDIA_URL,documento_root=settings.MEDIA_ROOT)



    