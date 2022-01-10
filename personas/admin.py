from django.contrib import admin
from django.db.models.aggregates import Count
from django.db.models.query_utils import Q
from django_admin_listfilter_dropdown.filters import (
    ChoiceDropdownFilter,
)

from escuela.admin import escuela_admin

from .actions import (
    exportar_datos_de_contacto_a_excel,
    exportar_datos_basicos_a_excel,
    exportar_todos_los_datos_a_excel,
    exportar_a_excel_datos_completos_de_responsables,
    exportar_a_excel_estudiantes_y_responsables_por_seccion,
    exportar_a_excel_estudiantes_y_responsables_por_familia_y_seccion,
)
from .filters import SeccionFilter, NivelEducativoFilter, MatriculadoFilter
from .models import (
    Departamento,
    Estudiante,
    Municipio,
    Responsable,
)


class EstudianteInline(admin.StackedInline):
    model = Estudiante
    fields = ["nombre", "apellidos", "seccion"]
    extra = 0
    verbose_name_plural = "Estudiantes a cargo"
    show_change_link = True

    def has_change_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj):
        return False

    def has_add_permission(self, request, obj):
        return False


class ResponsableAdmin(admin.ModelAdmin):
    search_fields = ["nombre", "apellidos", "dui"]
    list_display = ["__str__", "dui"]
    ordering = ["apellidos", "nombre"]
    inlines = [
        EstudianteInline,
    ]
    actions = [exportar_a_excel_datos_completos_de_responsables]

    def get_queryset(self, request):
        return super().get_queryset(request)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions


class SeccionInline(admin.TabularInline):
    model = Estudiante.secciones.through
    fields = ["seccion", "periodo_escolar"]
    readonly_fields = ["periodo_escolar"]
    verbose_name_plural = "Historial de secciones"

    def has_change_permission(self, requestt, obj):
        return False

    def has_add_permission(self, request, obj) -> bool:
        return False

    def has_delete_permission(self, request, obj):
        return False

    def periodo_escolar(self, obj):
        return obj.seccion.periodo_escolar

    periodo_escolar.short_description = "Período Escolar"


class EstudianteAdmin(admin.ModelAdmin):
    list_display = ["__str__", "seccion", "edad", "sobreedad", "sexo"]
    ordering = [
        "seccion__nivel_educativo__edad_normal_de_ingreso",
        "seccion",
        "apellidos",
        "nombre",
    ]
    list_filter = (
        ("sexo", ChoiceDropdownFilter),
        NivelEducativoFilter,
        SeccionFilter,
        "retirado",
        MatriculadoFilter,
    )
    inlines = [SeccionInline]
    search_fields = ["nombre", "apellidos"]
    autocomplete_fields = [
        "municipio_de_residencia",
        "municipio_de_nacimiento",
        "seccion",
        "escuela_previa",
        "estudiantes_en_la_misma_casa",
        "responsable",
    ]
    fieldsets = (
        (
            "Datos básicos del estudiante",
            {
                "fields": [
                    "nombre",
                    "apellidos",
                    "sexo",
                    "posee_partida",
                    "fecha_de_nacimiento",
                    "nacionalidad",
                    "municipio_de_nacimiento",
                    "estado_civil",
                ]
            },
        ),
        (
            "Información de contacto",
            {
                "fields": [
                    "telefono_1",
                    "telefono_2",
                    "correo_electronico",
                    "municipio_de_residencia",
                    "direccion_de_residencia",
                ]
            },
        ),
        (
            "Información escolar",
            {"fields": ["nie", "escuela_previa", "seccion"]},
        ),
        (
            "Información complementaria",
            {
                "fields": [
                    "trabaja",
                    "dependencia_economica",
                    "etnia",
                    "roommate",
                ]
            },
        ),
        (
            "Información sobre movilidad ciudadana",
            {
                "fields": [
                    "utiliza_vehiculo",
                    "utiliza_transporte_publico",
                    "camina_a_la_escuela",
                    "otro_medio_de_transporte",
                    "distancia",
                ]
            },
        ),
        (
            "Información de salud, seleccione cualquier condición que padezca el estudiante.",
            {
                "fields": [
                    "es_autista",
                    "sordera",
                    "ceguera",
                    "baja_vision",
                    "discapacidad_motora",
                    "discapacidad_intelectual",
                    "embarazo",
                    "down",
                    "otro",
                    "usa_medicamentos",
                    "medicamentos",
                    "tipo_de_sangre",
                ]
            },
        ),
        (
            "Servicios básicos y comunicaciones.",
            {
                "fields": [
                    "fuente_de_agua",
                    "piso",
                    "tipo_de_sanitario",
                    "posee_energia",
                    "posee_refrigerador",
                    "posee_televisor",
                    "posee_celular_con_acceso_a_internet",
                    "posee_radio",
                    "posee_computadora",
                    "posee_tablet",
                    "internet_residencial",
                    "compania_internet",
                ]
            },
        ),
        (
            "Situación familiar",
            {
                "fields": [
                    "cantidad_cohabitantes",
                    "menores_en_casa",
                    "responsable",
                    "relacion_de_responsable",
                    "estudiantes_en_la_misma_casa",
                ]
            },
        ),
        (
            "Retiro de estudiantes",
            {"fields": ["retirado", "fecha_de_retiro", "motivo_de_retiro"]},
        ),
    )
    actions = [
        exportar_datos_basicos_a_excel,
        exportar_datos_de_contacto_a_excel,
        exportar_todos_los_datos_a_excel,
        exportar_a_excel_estudiantes_y_responsables_por_seccion,
        exportar_a_excel_estudiantes_y_responsables_por_familia_y_seccion,
    ]

    class Media:
        js = ("hidePlus.js",)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions

    def get_queryset(self, request):
        search = request.GET.get("retirado__exact")
        change = request.GET.get("_changelist_filters")
        if search or change:
            return (
                super().get_queryset(request).select_related("seccion__nivel_educativo")
            )
        return (
            super()
            .get_queryset(request)
            .select_related("seccion__nivel_educativo")
            .filter(retirado=False)
        )


exportar_datos_basicos_a_excel.short_description = "Exportar datos básicos a excel"
exportar_a_excel_estudiantes_y_responsables_por_seccion.short_description = (
    "Exportar a Excel estudiantes y responsables ordenados por sección."
)
exportar_a_excel_estudiantes_y_responsables_por_familia_y_seccion.short_description = (
    "Exportar a Excel Estudiantes y Responsables ordenados por sección y familia"
)


class MunicipioAdmin(admin.ModelAdmin):
    search_fields = ["nombre"]
    list_display = ("__str__", "estudiantes_residentes")

    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions

    def get_queryset(self, request):
        return (
            super()
            .get_queryset(request)
            .prefetch_related("departamento")
            .annotate(_estudiantes_residentes=Count("reside_en", filter=Q(reside_en__seccion__isnull=False)))
            .order_by("-_estudiantes_residentes")
        )

    def estudiantes_residentes(self, obj):
        return obj._estudiantes_residentes


class DepartamentoAdmin(admin.ModelAdmin):
    search_fields = ["nombre"]

    def has_module_permission(self, request):
        return False


admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Responsable, ResponsableAdmin)


escuela_admin.register(Departamento, DepartamentoAdmin)
escuela_admin.register(Estudiante, EstudianteAdmin)
escuela_admin.register(Municipio, MunicipioAdmin)
escuela_admin.register(Responsable, ResponsableAdmin)
