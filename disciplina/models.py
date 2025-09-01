from django.db import models
from escuela.models import PeriodoEscolar

from personas.models import Estudiante


class Falta(models.Model):
    CATEGORIA_CHOICES = (("L", "Leve"), ("G", "Grave"), ("M", "Muy Grave"))
    codigo = models.PositiveSmallIntegerField(verbose_name="código")
    categoria = models.CharField(
        verbose_name="categoría", max_length=1, choices=CATEGORIA_CHOICES, default="L"
    )
    descripcion = models.TextField(verbose_name="descripción")

    def __str__(self):
        return f"{self.codigo} {self.get_categoria_display()} {self.descripcion[:50]}..."


class FaltaDisciplinariaEstudiantil(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    falta = models.ForeignKey(Falta, on_delete=models.CASCADE)
    fecha = models.DateField(help_text="Fecha en que se cometió la falta")
    descripcion = models.TextField(verbose_name="Descripción")
    periodo_escolar = models.ForeignKey(to=PeriodoEscolar, on_delete=models.PROTECT)
    docente_que_reporta = models.CharField(
        max_length=50, verbose_name="Docente que reporta", default=""
    )

    class Meta:
        verbose_name = "falta disciplinaria de estudiante"
        verbose_name_plural = "faltas disciplinarias de estudiantes"

    def __str__(self):
        return f"{self.falta.descripcion[:50]}..., {self.fecha}"

    def clean(self) -> None:
        self.periodo_escolar = PeriodoEscolar.objects.get(periodo_activo=True)


class Demerito(models.Model):
    codigo = models.CharField(verbose_name="código", max_length=3, unique=True)
    descripcion = models.CharField(verbose_name="descripción", max_length=100)

    class Meta:
        verbose_name = "demérito"
        verbose_name_plural = "deméritos"

    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"


class DemeritoDeEstudiante(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    demerito = models.ForeignKey(to=Demerito, on_delete=models.PROTECT)
    fecha = models.DateField(help_text="Fecha en que se cometió el demérito")
    descripcion = models.CharField(verbose_name="Descripción", max_length=150)
    periodo_escolar = models.ForeignKey(to=PeriodoEscolar, on_delete=models.PROTECT)
    docente_que_reporta = models.CharField(
        max_length=50, verbose_name="Docente que reporta", default=""
    )

    class Meta:
        verbose_name = "demérito de estudiante"
        verbose_name_plural = "deméritos de estudiantes"

    def __str__(self):
        return f"{self.falta.descripcion[:50]}..., {self.fecha}"
