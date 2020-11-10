from django.contrib import admin

from .mixins import ExportCsvMixin
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


class FamiliaAdminInline(admin.TabularInline):
    model = Familia
    autocomplete_fields = ['familiar', ]
    extra = 0


class ResponsableAdmin(admin.ModelAdmin):
    search_fields = ["nombre", "apellidos"]


class MenorDeEdadAdmin(admin.ModelAdmin):
    search_fields = ["nombre", "apellidos"]


class EstudiantesMenoresAdminInline(admin.TabularInline):
    model = EstudiantesYMenores
    autocomplete_fields = ["menor_de_edad"]
    extra = 0


class EstudianteAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ["__str__", "grado_matriculado", "seccion"]
    list_filter = ["grado_matriculado", "seccion"]
    search_fields = ["nombre", "apellidos"]
    autocomplete_fields = [
         "familiares", "estudiantes_en_la_misma_casa", 
         "responsable", "menores_cohabitantes"]
    inlines = [EstudiantesMenoresAdminInline, FamiliaAdminInline]
    ordering = ["grado_matriculado", "seccion", "apellidos", "nombre"]
    fieldsets = (
        ("Datos básicos del estudiante", {
            'fields': [
                "nombre", "apellidos", "sexo", 
                "posee_partida", "fecha_de_nacimiento",
                "nacionalidad", "municipio_de_nacimiento", "estado_civil",]
        }),
        ("Información de contacto", {
            'fields': [
                "telefono_1", "telefono_2", "correo_electronico",
                "municipio_de_residencia", "direccion_de_residencia"]
        }),
        ("Información escolar", {
            'fields': [
                 "nie", "escuela_previa", "seccion_previa",
                 "grado_matriculado", "seccion"]
        }),
        ("Información complementaria", {
            'fields': [
                "trabaja", "dependencia_economica",  "etnia", "roommate", ]
        }),
        ("Información sobre movilidad ciudadana", {
            'fields': [
                "utiliza_vehiculo",
                "utiliza_transporte_publico", "camina_a_la_escuela", 
                "otro_medio_de_transporte", "distancia", ]
        }),
        ("Información de salud, seleccione cualquier condición que padezca el estudiante.", {
            'fields': [
                "es_autista", "sordera", "ceguera", "baja_vision",
                "discapacidad_motora", "discapacidad_intelectual",
                "embarazo", "down", "otro",
                "usa_medicamentos", "medicamentos", "tipo_de_sangre"
            ]
        }),
        ("Servicios básicos y comunicaciones.", {
            'fields': [
                "fuente_de_agua", "piso", "tipo_de_sanitario",
                "posee_energia", "posee_refrigerador", "posee_televisor", 
                "posee_celular_con_acceso_a_internet", 
                "posee_radio", "posee_computadora", "posee_tablet", 
                "internet_residencial", "compania_internet", 
            ]
        }),
        ("Situación familiar", {
            'fields': [
                "cantidad_cohabitantes", "menores_en_casa",
                "responsable", "estudiantes_en_la_misma_casa",]
        }),
    )
    actions = ["exportar_a_excel", "exportar_a_excel_basico"]
    

admin.site.register(Departamento)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Familia, FamiliaAdmin)
admin.site.register(Municipio)
admin.site.register(Responsable, ResponsableAdmin)
admin.site.register(MenorDeEdad, MenorDeEdadAdmin)
