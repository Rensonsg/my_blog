from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.listar_post, name='listar_post'),
    path('post/<int:pk>/', views.detalle_post, name='detalle_post'),
    path('crear/', views.crear_post, name='crear_post'),
    path('editar/<int:pk>/', views.editar_post, name='editar_post'),
]
