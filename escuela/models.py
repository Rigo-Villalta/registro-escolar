from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Escuela(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(
        max_length=10, verbose_name="Código de infraestructura", blank=True, null=True
    )

    def __str__(self):
        return self.nombre


class PeriodoEscolar(models.Model):
    nombre = models.CharField(
        max_length=50,
        help_text='Ingrese el nombre del período escolar, por ejemplo: "Año escolar 2020',
    )
    fecha_de_inicio = models.DateField(
        help_text="Ingrese la fecha de inicio del período escolar"
    )
    fecha_de_cierre = models.DateField(
        help_text="Ingrese la fecha de cierre del período escolar"
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Períodos Escolares"


class NivelEducativo(models.Model):
    nivel = models.CharField(max_length=50)
    edad_normal_de_ingreso = models.PositiveSmallIntegerField(
        help_text="Ingrese la edad normal en que los estudiantes deben estar en este nivel educativo",
        validators=[
            MinValueValidator(2),
            MaxValueValidator(18),
        ],
    )

    def total_estudiantes(self):
        total = 0
        for seccion in self.seccion_set.all():
            total += seccion.estudiante_set.count()
        return total
    
    def total_femenino(self):
        total = 0
        for seccion in self.seccion_set.all():
            total += seccion.estudiante_set.filter(sexo="F").count()
        return total
    
    def total_masculino(self):
        total = 0
        for seccion in self.seccion_set.all():
            total += seccion.estudiante_set.filter(sexo="M").count()
        return total

    def __str__(self):
        return self.nivel

    def edad_de_ingreso_al_nivel(self):
        return f"{self.edad_normal_de_ingreso} años."

    class Meta:
        verbose_name_plural = "Niveles educativos."


class Seccion(models.Model):
    periodo_escolar = models.ForeignKey(
        PeriodoEscolar, verbose_name="período escolar", on_delete=models.CASCADE
    )
    nivel_educativo = models.ForeignKey(NivelEducativo, on_delete=models.CASCADE)
    SECCION_CHOICES = (("A", "A"), ("B", "B"), ("C", "C"), ("D", "D"), ("E", "E"))
    seccion = models.CharField(
        verbose_name="sección", max_length=1, choices=SECCION_CHOICES, default="A"
    )

    def total_estudiantes(self):
        return self.estudiante_set.count()
    
    def total_femenino(self):
        return self.estudiante_set.filter(sexo="F").count()
    
    def total_masculino(self):
        return self.estudiante_set.filter(sexo="M").count()

    def __str__(self):
        return f'{self.nivel_educativo} sección "{self.seccion}"'

    class Meta:
        verbose_name = "Sección"
        verbose_name_plural = "Secciones"
