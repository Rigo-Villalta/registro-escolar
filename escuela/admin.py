from django.contrib import admin
from django.db.models import Count, Q

from personas.models import Estudiante
from .actions import (
    exportar_datos_de_secciones,
    exportar_datos_de_grados,
    exportar_a_excel_lista_de_firma_por_seccion,
)
from .models import Escuela, NivelEducativo, Seccion, PeriodoEscolar


class EstudianteInline(admin.TabularInline):
    model = Estudiante
    fk_name = "seccion"
    fields = ["nombre", "apellidos", "sexo", "fecha_de_nacimiento"]
    extra = 0
    verbose_name_plural = "Estudiantes en la sección"
    show_change_link = True
    ordering = ["apellidos", "nombre"]

    def has_change_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj):
        return False

    def has_add_permission(self, request, obj):
        return False


class EscuelaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "codigo")
    search_fields = ["nombre"]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions


class NivelEducativoAdmin(admin.ModelAdmin):
    list_display = (
        "nivel",
        "edad_de_ingreso_al_nivel",
        "femenino",
        "masculino",
        "estudiantes_con_sobreedad",
        "estudiantes",
    )
    ordering = ["edad_normal_de_ingreso"]
    actions = [
        exportar_datos_de_grados,
    ]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _total_estudiantes=Count("seccion__estudiantes_en", distinct=True),
            _total_femenino=Count(
                "seccion__estudiantes_en", filter=Q(seccion__estudiantes_en__sexo="F")
            ),
            _total_masculino=Count(
                "seccion__estudiantes_en", filter=Q(seccion__estudiantes_en__sexo="M")
            )
        )
        return queryset

    def estudiantes(self, obj):
        return obj._total_estudiantes

    def femenino(self, obj):
        return obj._total_femenino

    def masculino(self, obj):
        return obj._total_masculino
    
    def estudiantes_con_sobreedad(self, obj):
        total = 0
        for seccion in obj.seccion_set.filter(periodo_escolar__periodo_activo=True):
            for estudiante in seccion.estudiantes_en.all():
                if estudiante.sobreedad():
                    total += 1
        return total

    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions


@admin.register(Seccion)
class SeccionAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "periodo_escolar",
        "femenino",
        "masculino",
        "estudiantes_con_sobreedad",
        "total_estudiantes"
    )
    ordering = [
        "nivel_educativo__edad_normal_de_ingreso",
        "nivel_educativo",
        "seccion",
    ]
    search_fields = ["__str__"]

    inlines = [
        EstudianteInline,
    ]
    actions = [exportar_datos_de_secciones, exportar_a_excel_lista_de_firma_por_seccion]

    def get_queryset(self, request):
        queryset = (
            super()
            .get_queryset(request)
            .filter(periodo_escolar__periodo_activo=True)
            .select_related("periodo_escolar", "nivel_educativo")
        )
        queryset = queryset.annotate(
            _total_estudiantes=Count("estudiantes_en", distinct=True),
            _total_femenino=Count("estudiantes_en", filter=Q(estudiantes_en__sexo="F")),
            _total_masculino=Count("estudiantes_en", filter=Q(estudiantes_en__sexo="M")),
        ).select_related("periodo_escolar")
        return queryset

    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
            return actions

    def total_estudiantes(self, obj):
        return obj._total_estudiantes

    def femenino(self, obj):
        return obj._total_femenino

    def masculino(self, obj):
        return obj._total_masculino
    
    def estudiantes_con_sobreedad(self, obj):
        total = 0
        for estudiante in obj.estudiantes_en.all():
            if estudiante.sobreedad():
                total += 1
        return total


admin.site.register(Escuela, EscuelaAdmin)
admin.site.register(NivelEducativo, NivelEducativoAdmin)
admin.site.register(PeriodoEscolar)
