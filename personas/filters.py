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
            return [
                (seccion.id, seccion.__str__)
                for seccion in Seccion.objects.filter(
                    nivel_educativo=search
                ).prefetch_related("nivel_educativo")
            ]
        else:
            return [
                (seccion.id, seccion.__str__)
                for seccion in Seccion.objects.all().prefetch_related("nivel_educativo")
            ]

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
        return [
            (nivel_educativo.id, nivel_educativo.__str__)
            for nivel_educativo in NivelEducativo.objects.all()
        ]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(grado_matriculado__id=self.value())