
from django import forms
from django.forms import ValidationError

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
class CategoriaForm(forms.Form):

    nombre = forms.CharField(
            label='Nombre', 
            max_length=50,
            validators=(solo_caracteres,),
            widget=forms.TextInput(attrs={'class':'form-control'})
        )   