from django.contrib import admin

# Register your models here.
#24/11 - 
from django.contrib.auth.admin import UserAdmin, GroupAdmin

from grupo2.models import Socio,CiudadResidencia, Comprobante, Cuota, Curso,Categoria 


#para agregagar los grupos de usuario y admin
from django.contrib.auth.models import User, Group



class grupo2AdminSite(admin.AdminSite):
    site_header = "Administración del CLUB"
    site_title = 'Club CED'
    index_title = 'Administración Principal'
    empty_value_display = 'NO hay Datos '

mi_admin = grupo2AdminSite(name='grupo2')

# mantener los grupos y usuarios en la pagina
mi_admin.register(Group)
mi_admin.register(User)

class grupo2UserSite(admin.AdminSite):
    site_header = "Carga de información del CLUB"
    site_title = 'Club CED'
    index_title = 'Carga Principal'
    empty_value_display = 'NO hay Datos '

mi_grupo2 = grupo2UserSite(name='grupo')

# Register your models here.
# son los modelos que se pueden manejar desde admin
#admin.site.register(Socio)
#admin.site.register(CiudadResidencia)

mi_grupo2.register(Comprobante)
mi_grupo2.register(Cuota)
mi_grupo2.register(Curso)
mi_grupo2.register(Categoria)



class SocioAdmin(admin.ModelAdmin):
    list_display = ('distintiva','nombre','apellido')

class CiudadResedenciaAdmin(admin.ModelAdmin):
    list_display = ('ciudad','provincia','codigoPostal')
#    list_editable = ('ciudad',)
    search_fields = ['ciudad','provincia']
    list_filter = ('ciudad','provincia')

mi_grupo2.register(Socio,SocioAdmin)
mi_grupo2.register(CiudadResidencia,CiudadResedenciaAdmin)

# Register your models here.
