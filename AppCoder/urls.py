from django.urls import path
from .views import *


urlpatterns = [
    path('curso/', curso),
    path('profesores/', profesores, name= 'profesores'),
    path('estudiantes/', estudiantes, name= 'estudiantes'),
    path('entregables/', entregables, name= 'entregables'),
    path('cursos/', cursos, name= 'cursos'),
    path('', inicio, name= 'inicio'),
    path('cursoFormulario/', cursoFormulario, name='cursoFormulario'),
    path('profeFormulario/', profeFormulario, name='profeFormulario'),
    path('busquedaComision/', busquedaComision, name='busquedaComision'),
    path('buscar/', buscar, name='buscar'),
    path('leerProfesores/', leerprofesores, name='leerprofesores'),
    path('eliminarProfesor/<nombre_profesor>', eliminarProfesor, name= 'eliminarProfesor'),
    path('editarProfesor/<nombre_profesor>', editarProfesor, name='editarProfesor'),

]