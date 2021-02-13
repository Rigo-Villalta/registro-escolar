from django.contrib import admin

from escuela.models import Seccion

class SeccionFilter(admin.SimpleListFilter):
    """
    Filtro usado para optimizar el acceso a las secciones
    dentro del filtro de estudiante
    """
    template = "django_admin_listfilter_dropdown/dropdown_filter.html"
    title = "Filtrar por sección"
    parameter_name = "seccion"

    def lookups(self, request, model_admin):
        """
        Aquí evitamos acceder a las llaves foraneas del model
        nos evitamos 1 consultas por cada instancia de Seccion
        """
        return [(seccion.id, seccion.seccion) for seccion in Seccion.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(seccion__id=self.value())