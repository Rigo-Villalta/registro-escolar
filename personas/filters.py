from django.contrib import admin

from escuela.models import NivelEducativo, Seccion


class SeccionFilter(admin.SimpleListFilter):
    """
    Filtro usado para optimizar el acceso a las secciones
    dentro del filtro de estudiante
    """

    template = "django_admin_listfilter_dropdown/dropdown_filter.html"
    title = "Sección"
    parameter_name = "seccion"

    def lookups(self, request, model_admin):
        """
        Aquí evitamos acceder a las llaves foraneas del model
        nos evitamos 1 consultas por cada instancia de Seccion
        """
        search = request.GET.get("nivel_educativo")
        if search:
            return Seccion.objects.select_related("nivel_educativo").filter(nivel_educativo=search).values_list("seccion", "id")
        else:
            return Seccion.objects.select_related("nivel_educativo").values_list("seccion", "id")

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(seccion__id=self.value())


class NivelEducativoFilter(admin.SimpleListFilter):
    """
    Filtro usado para optimizar el acceso a los niveles educativos
    dentro del filtro de estudiante
    """

    template = "django_admin_listfilter_dropdown/dropdown_filter.html"
    title = "Grado"
    parameter_name = "nivel_educativo"

    def lookups(self, request, model_admin):
        return NivelEducativo.objects.all().values_list("nivel", "id")

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(grado_matriculado__id=self.value())
