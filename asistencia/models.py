from django.db import models

from escuela.models import Seccion
from personas.models import Estudiante
   

class AsistenciaSeccion(models.Model):
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, limit_choices_to={"periodo_escolar__periodo_activo": True})
    fecha = models.DateField()

    class Meta:
        verbose_name = "Asistencia de sección"
        verbose_name_plural = "Asistencias de secciones"

    def __str__(self):
        return f"{self.seccion} - {self.fecha}"

class AsistenciaEstudiante(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, limit_choices_to={"activo": True})
    fecha = models.DateField()
    asistio = models.BooleanField()
    asistencia_de_seccion = models.ForeignKey(AsistenciaSeccion, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Asistencia de estudiante"
        verbose_name_plural = "Asistencias de estudiantes"

    def __str__(self):
        return f"{self.estudiante} - {self.fecha}"
