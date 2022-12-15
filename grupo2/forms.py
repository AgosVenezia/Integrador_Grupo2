
from django import forms
from django.forms import ValidationError
from grupo2.models import *
from .choices import *

# Ususarios del sistema
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User

from django.contrib.admin.widgets import AdminDateWidget





def solo_caracteres(valor):
    if any(char.isdigit() for char in valor):
        raise ValidationError("EL nombre no debe contener numeros: %(valor)s",
                            code='Error1',
                            params={'valor':valor})


class ContactoForm(forms.Form):
    nombre = forms.CharField(label='Nombre',
                             max_length=50,
                             validators=(solo_caracteres,),

                            widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el nombre'}))

    email = forms.EmailField(label='Email',max_length=50,
                            error_messages={
                                'requiered':'Por favor completa el campo',
                            },
                            widget=forms.TextInput(attrs={'class':'form-control','type':'email','placeholder':'Ingrese un email'}))

    asunto = forms.CharField(label='Asunto',max_length=100,
                            widget=forms.TextInput(attrs={'class':'form-control',}))
                            
    mensaje = forms.CharField(label='Mensaje',max_length=500,
                            widget=forms.Textarea(attrs={'class':'form-control','rows':5}))

    suscripcion= forms.BooleanField(label=' Suscribirse a las novedades ', required=False,
                            widget=forms.CheckboxInput(attrs={'class':'form-check-input','value':1}))

    
    def clean_mensaje(self):
        data = self.cleaned_data['mensaje']
        if len(data) < 10:
            raise ValidationError("Agrega mas comentarios para poder ayudarte: %(valor1)s",
                            code='Error2',
                            params={'valor1':data})
        return data

    def clean(self):
        cleaned_data = super().clean()
        mensaje = cleaned_data.get("mensaje")
        asunto = cleaned_data.get('asunto')

        #if "ayuda" not in asunto or "ayuda" not in mensaje:
        #    msg= "Debe agregar la palabra -ayuda- en el campo."
        #    self.add_error('asunto',msg)
        #    self.add_error('mensaje',msg)


    

#-- modificado 08/11
#class CategoriaForm(forms.Form):

#    nombre = forms.CharField(
#            label='Nombre', 
#            max_length=50,
#            validators=(solo_caracteres,),
#            widget=forms.TextInput(attrs={'class':'form-control'})
   #     )   


class CategoriaForm(forms.ModelForm):
    
    class Meta:
        model=Categoria
        fields ='__all__'
    #    exclude = ('baja',)

#  Ciudades de residencia de los SOCIOS
class CiudadForm(forms.ModelForm):
    
    class Meta:
        model=CiudadResidencia
        fields ='__all__'
        exclude = ('baja',)

#  Comprobantes de pago
class ComprobanteForm(forms.ModelForm):
    
    class Meta:
        model=Comprobante 
        fields = '__all__'
        comprobante = forms.CharField(max_length=64),
        fecha = forms.DateField(widget=AdminDateWidget),
        montoComprobante = forms.FloatField,
        observaciones = forms.Textarea,
            

        

        widgets = {
            'comprobante':forms.TextInput(attrs={'class':'form-control'}),
            'fecha':forms.DateField(widget=AdminDateWidget()),       
                
            'montoComprobante':forms.FloatField(),
            'observaciones':forms.Textarea(attrs={'class':'form-control'}),
        }

        exclude = ('baja',)



#  CUOTAS  de los SOCIOS
class CuotaForm(forms.ModelForm):
    
    class Meta:
        model=Cuota
        fields ='__all__'
        #cuota=forms.TextInput()  # numero de cuota  año+mes ej: 202003
       # socio=forms.ModelChoiceField(queryset=Socio.objects.distinct('distintiva'))  # referencia con tabla socio a quien corresponde la cuota
       # comprobante=forms.ModelChoiceField(queryset=Comprobante.objects.distinct('comprobante'))
       # montoCuota=forms.FloatField()  # monto de la cuota que se abono
        exclude = ('baja',)

    

#  Cursos del Club
class CursoForm(forms.ModelForm):
    
    class Meta:
        model=Curso
        fields =['nombre','dia','turno']
        
        def __init__ (self, *args, **kwargs):
            super().__init__( *args, **kwargs)

            self.fields['nombre'].widget.attrs.update({
                'class':'form-control',                
                })

            self.fields['dia'].widget.attrs.update({
                'class':'form-control',                
                })

            






#  inicio de socios
class SocioForm(forms.ModelForm):
    
    class Meta:
        model=Socio
        fields ='__all__'
        # fields = ['nombrecampo1','nombrede campo 2']
        exclude = ('baja',)


#========================================
#Usuarios

class RegistrarUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name' ,'email']


class CambiarContraseniaForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["old_password"] = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}), required=False)
        self.fields["new_password1"].widget = forms.PasswordInput(attrs={"class": "form-control"})
        self.fields["new_password2"].widget = forms.PasswordInput(attrs={"class": "form-control"})   


