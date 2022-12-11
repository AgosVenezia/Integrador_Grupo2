from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_grupo2 import views

router = DefaultRouter()
router.register(r'socios', views.SocioViewSet, basename='socio')

urlpatterns = [
    path('', include(router.urls)),
    path('curso/', views.categoria_list),
    path('curso/<int:pk>/', views.categoria_detail),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]






