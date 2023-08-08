from django.urls import path, include #Agregué include
from.views import *

urlpatterns = [
    path('', home, name="home"), 
    path('cursos/', cursos, name="cursos"), 
    path('profesores/', profesores, name="profesores"), 
    path('estudiantes/', estudiantes, name="estudiantes"), 
    path('entregables/', entregables, name="entregables"), 
]