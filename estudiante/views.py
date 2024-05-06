from django.http import JsonResponse #Nos vas a mostrar la info en formato Json
from django.shortcuts import render, get_object_or_404

from estudiante.models import Estudiante, Curso #siempre hay que importar los modelos


def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all()

    # Serializar cada instancia de Estudiante a JSON
    estudiantes_data = [estudiante.to_json() for estudiante in estudiantes]

    # Devolver los datos serializados como una respuesta JSON
    return JsonResponse(estudiantes_data, status=200, safe=False)


def listar_estudiantes_segun_edad(request, edad):
    filtro_estudiantes = Estudiante.objects.filter(edad__gt=edad)

    # Serializar cada instancia de Estudiante a JSON
    estudiantes_data = [estudiante.to_json() for estudiante in filtro_estudiantes]

    # Devolver los datos serializados como una respuesta JSON
    return JsonResponse(estudiantes_data, status=200, safe=False)


def detalle_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)

    alumnos_curso = curso.estudiantes.all()

    # Serializar cada instancia de Estudiante a JSON
    alumnos_curso_data = [estudiante.to_json() for estudiante in alumnos_curso]

    curso_data = curso.to_json()

    curso_data['estudiantes'] = alumnos_curso_data

    return JsonResponse(curso_data, status=200, safe=False)


def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'estudiante/lista_cursos.html', {'cursos': cursos})
