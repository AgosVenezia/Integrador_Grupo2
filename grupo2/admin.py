from django.contrib import admin

# Register your models here.
#24/11 - 
from django.contrib.auth.admin import UserAdmin, GroupAdmin

from grupo2.models import Socio,CiudadResidencia, Comprobante, Cuota, Curso,Categoria ,Inscripcion


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

# ---------------------------------------------------------------------------

# Register your models here.
# son los modelos que se pueden manejar desde admin
#admin.site.register(Socio)
#admin.site.register(CiudadResidencia)




mi_grupo2.register(Categoria)
mi_grupo2.register(Inscripcion)


class SocioAdmin(admin.ModelAdmin):
    list_display = ('distintiva','nombre','apellido')
    search_fields = ['nombre','apellido','distintiva']
    list_filter = ('idCategoriaSocio','categoriaDistintiva','condicionDePago','ciudadResidencia')

    

class CiudadResedenciaAdmin(admin.ModelAdmin):
    list_display = ('ciudad','provincia','codigoPostal')
#    list_editable = ('ciudad',)
    search_fields = ['ciudad','provincia']
    list_filter = ('ciudad','provincia','codigoPostal')

class CuotaAdmin(admin.ModelAdmin):
    list_display = ('socio','cuota','montoCuota','comprobante')
#    list_editable = ('ciudad',)
    search_fields = ['socio','cuota','comprobante']
    list_filter = ('socio','comprobante')

class ComprobanteAdmin(admin.ModelAdmin):
    list_display = ('fecha','comprobante','montoComprobante','observaciones')
#    list_editable = ('ciudad',)
    search_fields = ['fecha','comprobante']
    list_filter = ('fecha','comprobante')

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre','categoria','descripcion')
#    list_editable = ('ciudad',)
    search_fields = ['nombre','categoria']
    list_filter = ('nombre','categoria','baja')

    # modificar el estado de relacion, no aparecen las opciones que esten de BAJA
    def formfield_for_foreignkey(self, db_field,  request, **kwargs):
        if db_field.name=='categoria':
            kwargs['queryset'] = Categoria.objects.filter(baja=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # MODficar el estado de many to many
    #def formfield_for_foreignkey(self, db_field,  request, **kwargs):
    #    if db_field.name=='socio':
     #       kwargs['queryset'] = Socio.objects.filter()
     #   return super().formfield_for_foreignkey(db_field, request, **kwargs) 

class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('fecha_creacion','curso','socio','estado')
#    list_editable = ('ciudad',)
    search_fields = ['fecha_creacion','curso','socio','estado']
    list_filter = ('fecha_creacion','curso','socio','estado')

    # modificar el estado de relacion, no aparecen las opciones que esten de BAJA
    def formfield_for_foreignkey(self, db_field,  request, **kwargs):
        if db_field.name=='curso':
            kwargs['queryset'] = Curso.objects.filter(baja=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    

mi_grupo2.register(Socio,SocioAdmin)
mi_grupo2.register(CiudadResidencia,CiudadResedenciaAdmin)
mi_grupo2.register(Cuota,CuotaAdmin)
mi_grupo2.register(Comprobante,ComprobanteAdmin)
mi_grupo2.register(Curso,CursoAdmin)
# Register your models here.

mi_grupo2.register(User,UserAdmin)
mi_grupo2.register(Group,GroupAdmin)
