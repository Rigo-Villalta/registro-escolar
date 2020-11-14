from django.contrib import admin

from .models import Falta, FaltaDisciplinariaEstudiantil

class FaltaAdmin(admin.ModelAdmin):
    list_display = ['codigo', "categoria", "descripcion"]


class FaltaDisciplinariaEstudiantilAdmin(admin.ModelAdmin):
    list_display = ["estudiante", "__str__"]
    autocomplete_fields = ['estudiante']
    search_fields = ["estudiante__nombre", "estudiante__apellidos"]


admin.site.register(Falta, FaltaAdmin)
admin.site.register(FaltaDisciplinariaEstudiantil, FaltaDisciplinariaEstudiantilAdmin)