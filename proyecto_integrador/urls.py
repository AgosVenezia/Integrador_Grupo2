"""proyecto_integrador URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.urls.conf import include

from grupo2.admin import mi_admin,mi_grupo2

urlpatterns = [
    # el nombre admin/ e la maera de llamar el acceso y se puede cambiar

    #por defecto 
    # path('admin/', admin.site.urls),

    path('admin/', mi_admin.urls),
    path("",include("grupo2.urls")),
    
    #Se peuden tener 2 opciones de admin
    path('grupo/', mi_grupo2.urls)
]
