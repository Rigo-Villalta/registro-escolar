from django.contrib import admin

from escuela.models import PeriodoEscolar
from escuela.admin import escuela_admin

from .models import Falta, FaltaDisciplinariaEstudiantil


class FaltaAdmin(admin.ModelAdmin):
    list_display = ["codigo", "categoria", "descripcion"]


class FaltaDisciplinariaEstudiantilAdmin(admin.ModelAdmin):
    list_display = ["estudiante", "fecha", "descripcion"]
    autocomplete_fields = ["estudiante"]
    search_fields = ["estudiante__nombre", "estudiante__apellidos"]


class FaltaDisciplinariaEstudiantilInline(admin.TabularInline):
    model = FaltaDisciplinariaEstudiantil
    fields = ["falta", "fecha"]
    readonly_fields = ["falta", "fecha"]
    extra = 0
    show_change_link = True
    verbose_name_plural = "Faltas disciplinarias cometidas por el estudiante"
    template = "admin/faltas_de_estudiante_inline.html"

    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj):
        return False

    def get_queryset(self, request):
        periodo_escolar_activo = PeriodoEscolar.objects.get(periodo_activo=True)
        return (
            super()
            .get_queryset(request)
            .filter(fecha__gt=periodo_escolar_activo.fecha_de_inicio)
        )


admin.site.register(Falta, FaltaAdmin)
admin.site.register(FaltaDisciplinariaEstudiantil, FaltaDisciplinariaEstudiantilAdmin)

escuela_admin.register(Falta, FaltaAdmin)
escuela_admin.register(
    FaltaDisciplinariaEstudiantil, FaltaDisciplinariaEstudiantilAdmin
)
