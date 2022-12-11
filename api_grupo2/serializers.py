from rest_framework import serializers
from grupo2.models import Socio,Curso

class SocioSerializer(serializers.ModelSerializer):


    class Meta:
        model = Socio
        fields = ['id','nombre','apellido','distintiva','dni','email']


class CursoSerializer(serializers.ModelSerializer):


    class Meta:
        model = Curso
        fields = ['id','nombre','categoria','descripcion','imagen']