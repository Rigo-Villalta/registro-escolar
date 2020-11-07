from django.contrib import admin

from .models import Escuela, NivelEducativo, Seccion, PeriodoEscolar

class EscuelaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo')


class NivelEducativoAdmin(admin.ModelAdmin):
    list_display = ("nivel", "edad_de_ingreso_al_nivel")
    ordering = ["edad_normal_de_ingreso"]


class SeccionAdmin(admin.ModelAdmin):
    list_display = ("__str__", "periodo_escolar")
    ordering = ["periodo_escolar__fecha_de_cierre", "nivel_educativo__edad_normal_de_ingreso"]


admin.site.register(Escuela, EscuelaAdmin)
admin.site.register(NivelEducativo, NivelEducativoAdmin)
admin.site.register(Seccion, SeccionAdmin)
admin.site.register(PeriodoEscolar)
