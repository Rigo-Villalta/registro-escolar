from django.contrib import admin

from .models import Escuela, NivelEducativo, Seccion, PeriodoEscolar

class EscuelaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo')


class NivelEducativoAdmin(admin.ModelAdmin):
    list_display = ("nivel", "edad_de_ingreso_al_nivel", "masculino", "femenino", "estudiantes")
    ordering = ["edad_normal_de_ingreso"]


class SeccionAdmin(admin.ModelAdmin):
    list_display = ("__str__", "estudiantes", 'femenino', 'masculino')
    ordering = ["periodo_escolar__fecha_de_cierre", "nivel_educativo__edad_normal_de_ingreso", "seccion"]


admin.site.register(Escuela, EscuelaAdmin)
admin.site.register(NivelEducativo, NivelEducativoAdmin)
admin.site.register(Seccion, SeccionAdmin)
admin.site.register(PeriodoEscolar)
