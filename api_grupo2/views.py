from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from grupo2.models import Socio,Curso
from api_grupo2 import serializers

# Create your views here.

from api_grupo2.serializers import CursoSerializer,SocioSerializer

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response

# Create your views here.
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all().order_by('id')
    serializer_class = serializers.CursoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def categoria_list(request):
    """
    Lista todos los proyecto, o crea un nuevo proyecto.
    """
    if request.method == 'GET':
        categorias = Curso.objects.filter(baja=False)
        serializer = CursoSerializer(categorias, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid():
            #agrega mi logica
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def categoria_detail(request, pk):
    """
    Muestra, actualiza o elimina una categoria.
    """
    try:
        categoria = Curso.objects.get(pk=pk)
    except Curso.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CursoSerializer(categoria)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CursoSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Curso.soft_delete()
        return Response({'message':'Se elimino la categoria'},status=status.HTTP_204_NO_CONTENT)

#class Socio(viewsets.ModelViewSet):
 #   queryset = Socio.objects.all().order_by('id')
 #   serializer_class = serializers.SocioSerializer
 #   permission_classes = [permissions.IsAuthenticatedOrReadOnly]



# Create your views here.
class SocioViewSet(viewsets.ModelViewSet):
    queryset = Socio.objects.all().order_by('id')
    serializer_class = serializers.SocioSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
