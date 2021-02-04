import codecs
import csv

from django.contrib import admin
from django.http import HttpResponse

from django_admin_listfilter_dropdown.filters import (
    DropdownFilter,
    ChoiceDropdownFilter,
    RelatedDropdownFilter,
)

from .actions import (
    exportar_datos_de_contacto_a_excel,
    exportar_datos_basicos_a_excel,
    exportar_todos_los_datos_a_excel,
)

from .models import (
    Departamento,
    Estudiante,
    Familia,
    MenorDeEdad,
    EstudiantesYMenores,
    Municipio,
    Responsable,
)


class FamiliaAdmin(admin.ModelAdmin):
    list_display = ["estudiante", "familiar", "relacion"]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions


class FamiliaAdminInline(admin.TabularInline):
    model = Familia
    autocomplete_fields = [
        "familiar",
    ]
    extra = 0


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
    search_fields = ["nombre", "apellidos"]
    list_display = ["__str__", "dui"]
    inlines = [
        EstudianteInline,
    ]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions


class MenorDeEdadAdmin(admin.ModelAdmin):
    search_fields = ["nombre", "apellidos"]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions


class EstudiantesMenoresAdminInline(admin.TabularInline):
    model = EstudiantesYMenores
    autocomplete_fields = ["menor_de_edad"]
    extra = 0


class EstudianteAdmin(admin.ModelAdmin):
    list_display = ["__str__", "grado_matriculado", "seccion", "edad", "sexo"]
    ordering = [
        "grado_matriculado__edad_normal_de_ingreso",
        "seccion",
        "apellidos",
        "nombre",
    ]
    list_filter = (
        ("sexo", ChoiceDropdownFilter),
        ("grado_matriculado", RelatedDropdownFilter),
        ("seccion", RelatedDropdownFilter),
    )
    # ["grado_matriculado", "seccion"]
    search_fields = ["nombre", "apellidos"]
    autocomplete_fields = [
        "municipio_de_residencia",
        "municipio_de_nacimiento",
        "escuela_previa",
        "familiares",
        "estudiantes_en_la_misma_casa",
        "responsable",
        "menores_cohabitantes",
    ]
    inlines = [EstudiantesMenoresAdminInline, FamiliaAdminInline]
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
            {
                "fields": [
                    "nie",
                    "escuela_previa",
                    "seccion_previa",
                    "grado_matriculado",
                    "seccion",
                ]
            },
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
    )
    actions = [
        exportar_datos_basicos_a_excel,
        exportar_datos_de_contacto_a_excel,
        exportar_todos_los_datos_a_excel,
    ]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions


exportar_datos_basicos_a_excel.short_description = "Exportar datos básicos a excel."


class MunicipioAdmin(admin.ModelAdmin):
    search_fields = ["nombre"]
    ordering = ["id"]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions


admin.site.register(Departamento)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Familia, FamiliaAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Responsable, ResponsableAdmin)
admin.site.register(MenorDeEdad, MenorDeEdadAdmin)
