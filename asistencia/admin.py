from django.contrib import admin

from escuela.admin import escuela_admin

from .models import AsistenciaEstudiante, AsistenciaSeccion


# AsistenciaEstudiante es un inline de AsistenciaSeccion, cuando
# se crea una asistencia de sección, se pueden agregar asistencias
# de estudiantes en la misma página.

class AsistenciaEstudianteInline(admin.TabularInline):
    model = AsistenciaEstudiante
    extra = 0
    fields = ["estudiante", "asistio"]
    readonly_fields = ["estudiante"]
    can_delete = False


class AsistenciaSeccionAdmin(admin.ModelAdmin):
    inlines = [AsistenciaEstudianteInline]
    list_display = ["seccion", "fecha"]
    list_filter = ["seccion__nivel_educativo", "seccion", "fecha"]
    search_fields = ["seccion__nivel_educativo__nivel", "seccion__seccion"]
    date_hierarchy = "fecha"
    ordering = ["seccion", "fecha"]

    def save_model(self, request, obj, form, change):
        # Al guardar la asistencia de sección, se crean todas las asistencias
        # de estudiantes de la sección.
        super().save_model(request, obj, form, change)
        if not obj.asistenciaestudiante_set.all():
            for estudiante in obj.seccion.estudiantes.all():
                AsistenciaEstudiante.objects.create(
                    estudiante=estudiante, fecha=obj.fecha, asistio=True, asistencia_de_seccion=obj
                )



escuela_admin.register(AsistenciaSeccion, AsistenciaSeccionAdmin)