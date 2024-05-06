from django.urls import path

from .views import listar_estudiantes, listar_estudiantes_segun_edad, detalle_curso, listar_cursos

app_name = 'estudiante'

urlpatterns = [
    path('listar-estudiantes', listar_estudiantes, name='listado-estudiantes'),
    path('listar-edad-mayor-a/<int:edad>/', listar_estudiantes_segun_edad, name='listado-estudiantes-segun-edad'),
    path('detalle-curso/<int:pk>/', detalle_curso, name='detalle-curso'),
    path('lista-cursos/', listar_cursos, name='lista-cursos')

]