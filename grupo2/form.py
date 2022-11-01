
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
                            widget=forms.TextInput(attrs={'class':'form-control','type':'email','placeholder':'Ingrese un email'}))
    asunto = forms.CharField(label='Asunto',max_length=100,
                            widget=forms.TextInput(attrs={'class':'form-control',}))
    mensaje = forms.CharField(label='Mensaje',max_length=500,
                            widget=forms.Textarea(attrs={'class':'form-control','rows':5}))

    suscripcion= forms.BooleanField(label=' Suscribirse a las Novedades ', required=False,
                            widget=forms.CheckboxInput(attrs={'class':'form-check-input','value':1}))

    
    def clean_mensaje(self):
        data = self.cleaned_data['mensaje']
        if len(data) < 10:
            raise ValidationError('Es importante que nos expreses bien tu cunsulta')
        return data
