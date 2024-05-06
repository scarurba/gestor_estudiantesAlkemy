from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad_horas_dictado = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nombre

    def to_json(self):  #Este método crea un diccionario de todo lo que se recopila en la clase Curso
        curso_json = {
            'nombre': self.nombre,
            'cantidad_horas_dictado': float(self.cantidad_horas_dictado),
        }

        return curso_json #Esto se va a mostrar en la vista, luego cuando se llame JsonResponse


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.PositiveSmallIntegerField()
    nota_curso = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='estudiantes') #la relacion uno a muchos

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'

    def to_json(self):
        return {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad,
            'nota_curso': float(self.nota_curso),  # Convertir a float para serializar correctamente
            'curso': self.curso.to_json()
        }