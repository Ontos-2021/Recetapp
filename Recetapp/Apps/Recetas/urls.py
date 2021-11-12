from django.urls import path

from . import views

app_name = 'recetas'
urlpatterns = [
    path('', views.index, name='index'),
    path('recetas/', views.recetas, name='recetas'),
    path('crear-receta', views.crear_receta, name='crear-receta'),
    path('guardar_receta', views.guardar_receta, name='guardar-receta')
]
