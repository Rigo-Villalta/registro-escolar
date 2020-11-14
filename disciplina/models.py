from django.db import models

from personas.models import Estudiante

class Falta(models.Model):
    CATEGORIA_CHOICES = (
        ('L', 'Leve'),
        ('G', 'Grave'),
        ('M', "Muy Grave")
    )
    codigo = models.PositiveSmallIntegerField(verbose_name="código")
    categoria = models.CharField(verbose_name="categoría", max_length=1, choices=CATEGORIA_CHOICES, default='L')
    descripcion = models.TextField(verbose_name="descripción")

    def __str__(self):
        return self.descripcion


class FaltaDisciplinariaEstudiantil(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    falta = models.ForeignKey(Falta, on_delete=models.CASCADE)
    fecha = models.DateField(help_text="Fecha en que se cometió la falta")
    descripcion = models.TextField(verbose_name="Descripción")

    class Meta:
        verbose_name = "Falta disciplinaria de estudiante"
        verbose_name_plural = "Faltas disciplinarias de estudiantes"

    def __str__(self):
        return f'{self.falta.descripcion}, {self.fecha}'
