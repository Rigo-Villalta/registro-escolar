from django.contrib import admin
from django.db.models import Count, Q

from .models import Escuela, NivelEducativo, Seccion, PeriodoEscolar


class EscuelaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "codigo")
    search_fields = ["nombre"]


class NivelEducativoAdmin(admin.ModelAdmin):
    list_display = (
        "nivel",
        "edad_de_ingreso_al_nivel",
        "femenino",
        "masculino",
        "estudiantes",
    )
    ordering = ["edad_normal_de_ingreso"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _total_estudiantes=Count("seccion__estudiante", distinct=True),
            _total_femenino=Count("seccion__estudiante", filter=Q(seccion__estudiante__sexo="F")),
            _total_masculino=Count("seccion__estudiante", filter=Q(seccion__estudiante__sexo="M")),
        )
        return queryset

    def estudiantes(self, obj):
        return obj._total_estudiantes

    def femenino(self, obj):
        return obj._total_femenino

    def masculino(self, obj):
        return obj._total_masculino


@admin.register(Seccion)
class SeccionAdmin(admin.ModelAdmin):
    list_display = ("__str__", "femenino", "masculino", "estudiantes")
    ordering = [
        "nivel_educativo__edad_normal_de_ingreso",
        "nivel_educativo",
        "seccion",
    ]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _total_estudiantes=Count("estudiante", distinct=True),
            _total_femenino=Count("estudiante", filter=Q(estudiante__sexo="F")),
            _total_masculino=Count("estudiante", filter=Q(estudiante__sexo="M")),
        )
        return queryset

    def estudiantes(self, obj):
        return obj._total_estudiantes

    def femenino(self, obj):
        return obj._total_femenino

    def masculino(self, obj):
        return obj._total_masculino


admin.site.register(Escuela, EscuelaAdmin)
admin.site.register(NivelEducativo, NivelEducativoAdmin)
admin.site.register(PeriodoEscolar)
