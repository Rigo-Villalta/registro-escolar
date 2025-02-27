from django.contrib import admin
from django.utils.text import capfirst
from django.db.models import Count, Q
from django.db.models.query import Prefetch

from personas.models import Estudiante
from .actions import (
    exportar_datos_de_secciones,
    exportar_datos_de_grados,
    exportar_a_excel_lista_de_firma_por_seccion,
)

from .filters import SeccionPorPeriodoFilter
from .models import Escuela, NivelEducativo, Seccion, PeriodoEscolar


class EscuelaAdmin(admin.AdminSite):
    """
    Us sitio administrativo derivado de Django Admin con el propósito
    de sobreescribir ciertos comportamientos.
    """

    def get_app_list(self, request):
        """
        RIGO: He sobreescrito este método para que se pueda hacer un orden
        personalizado de los modelos y aplicaciones en el índice del admin.
        Para ello es necesario ingresar el verbose_name_plural de cada
        aplicación o model como clave de los diccionarios 'ordering apps' y
        'ordering_models'respectivamente y el número de prioridad que le
        queremos dar como valor. Dos modelos pueden tener el mismo número
        de prioridad si son de diferentes aplicaciones.
        OJO: Es responsabilidad del programador ingresar las aplicaciones y
        modelos que se registran en el SchoolAdmin o se obtendrá
        un error de ejecución al correr el sitio.
        """
        ordering_apps = {"usuarios": 1, "personas": 2, "escuela": 3, "disciplina": 4, "asistencia": 5}
        # En ordering_models es importante usar capfirst para que iguale
        # el diccionario creado por el método _build_app_dict
        ordering_models = {
            # Users
            capfirst("usuarios"): 1,
            # Personas
            capfirst("estudiantes"): 1,
            capfirst("responsables"): 2,
            capfirst("municipios"): 3,
            # Escuela
            capfirst("escuelas"): 1,
            capfirst("períodos escolares"): 2,
            capfirst("niveles educativos"): 3,
            capfirst("secciones"): 4,
            # Disciplina
            capfirst("faltas"): 1,
            capfirst("Faltas disciplinarias de estudiantes"): 2,
            #asistencia
            capfirst("asistencias de secciones"): 1,
        }
        app_dict = self._build_app_dict(request)
        # Se sobreescribe el orden de las apps
        app_list = sorted(
            app_dict.values(), key=lambda x: ordering_apps[x["name"].lower()]
        )

        # Se sobreescribe el orden de los modelos
        for app in app_list:
            app["models"].sort(key=lambda x: ordering_models[x["name"]])

        return app_list


escuela_admin = EscuelaAdmin(name="escuela_admin")


class EstudianteInline(admin.TabularInline):
    model = Estudiante
    fk_name = "seccion"
    fields = ["apellidos", "nombre", "retirado"]
    extra = 0
    verbose_name_plural = "Estudiantes en la sección"
    show_change_link = True
    ordering = ["apellidos", "nombre"]

    def has_change_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj):
        if obj is not None:
            return obj.periodo_escolar.periodo_activo
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
            ),
        )
        return queryset

    def estudiantes(self, obj):
        return obj._total_estudiantes

    def femenino(self, obj):
        return obj._total_femenino

    def masculino(self, obj):
        return obj._total_masculino

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
        "activos",
        "retirados",
        "retirados_femenino",
        "retirados_masculino"
    )
    search_fields = ["nivel_educativo__nivel"]
    list_filter = [SeccionPorPeriodoFilter]
    inlines = [
        EstudianteInline,
    ]
    actions = [exportar_datos_de_secciones, exportar_a_excel_lista_de_firma_por_seccion]

    def get_queryset(self, request):
        # filter = request.GET.get("periodo_escolar")
        queryset = (
            Seccion.objects.select_related("periodo_escolar", "nivel_educativo")
            .prefetch_related(Prefetch("estudiantes"))
            .annotate(
                _activos=Count("estudiantes", filter=Q(estudiantes__retirado=False)),
                _femenino=Count("estudiantes", filter=Q(estudiantes__sexo="F")),
                _masculino=Count("estudiantes", filter=Q(estudiantes__sexo="M")),
                _retirados_masculino=Count("estudiantes", filter=Q(estudiantes__retirado=True, estudiantes__sexo="M")),
                _retirados_femenino=Count("estudiantes", filter=Q(estudiantes__retirado=True, estudiantes__sexo="F")),
                _retirados=Count("estudiantes", filter=Q(estudiantes__retirado=True))
            )
        ).order_by(
            "nivel_educativo__edad_normal_de_ingreso", "nivel_educativo", "seccion"
        )
        return queryset

    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
            return actions

    def get_search_results(self, request, queryset, search_term):
        """
        Sobreescribimos este método para que los resultados de la búsqueda
        """
        queryset, use_distinct = super().get_search_results(
            request, queryset, search_term
        )
        url_referida = request.META.get("HTTP_REFERER").rstrip("/").split("/")
        # este if es necesario  para evitar que al estar en la ChangeView de un
        # Estudiantes, el queryset no contenga los atributos "Annotate" que se han
        # pueste en get_queryset.
        try:
            if "autocomplete" in request.path and url_referida[5] == "estudiante" and url_referida[7] == "change":
                try:
                    id_estudiante = url_referida[6]
                    estudiante = Estudiante.objects.get(pk=id_estudiante)
                    seccion_mayor = estudiante.secciones.filter(
                        periodo_escolar__periodo_activo=False
                    ).order_by("-nivel_educativo__edad_normal_de_ingreso")[0]
                    if seccion_mayor.nivel_educativo.nivel == "EDUCACIÓN ACELERADA":
                        queryset = (
                            Seccion.objects.select_related(
                                "nivel_educativo", "periodo_escolar"
                            )
                            .filter(
                                Q(periodo_escolar__periodo_activo=True),
                                Q(nivel_educativo__edad_normal_de_ingreso=11)
                                | Q(nivel_educativo__edad_normal_de_ingreso=12)
                                | Q(nivel_educativo__edad_normal_de_ingreso=13)
                            )
                            .order_by(
                                "nivel_educativo__edad_normal_de_ingreso",
                                "nivel_educativo",
                                "seccion",
                            )
                        )
                    elif 7 < seccion_mayor.nivel_educativo.edad_normal_de_ingreso < 12:
                        queryset = (
                            Seccion.objects.select_related(
                                "nivel_educativo", "periodo_escolar"
                            )
                            .filter(
                                Q(periodo_escolar__periodo_activo=True),
                                Q(nivel_educativo=seccion_mayor.nivel_educativo)
                                | Q(
                                    nivel_educativo__edad_normal_de_ingreso=seccion_mayor.nivel_educativo.edad_normal_de_ingreso
                                    + 1
                                )
                                | Q(nivel_educativo__edad_normal_de_ingreso=12),
                            )
                            .order_by(
                                "nivel_educativo__edad_normal_de_ingreso",
                                "nivel_educativo",
                                "seccion",
                            )
                        )
                    else:
                        queryset = (
                            Seccion.objects.select_related(
                                "nivel_educativo", "periodo_escolar"
                            )
                            .filter(
                                Q(periodo_escolar__periodo_activo=True),
                                Q(nivel_educativo__edad_normal_de_ingreso=seccion_mayor.nivel_educativo.edad_normal_de_ingreso)
                                | Q(
                                    nivel_educativo__edad_normal_de_ingreso=seccion_mayor.nivel_educativo.edad_normal_de_ingreso
                                    + 1
                                ),
                            )
                            .order_by(
                                "nivel_educativo__edad_normal_de_ingreso", "seccion"
                            )
                        )
                except:
                    pass
        except:
            pass
        return queryset, use_distinct

    def activos(self, obj):
        return obj._activos

    def femenino(self, obj):
        return obj._femenino

    def masculino(self, obj):
        return obj._masculino
    
    def retirados(self, obj):
        return obj._retirados
    
    def retirados_masculino(self, obj):
        return obj._retirados_masculino
    
    def retirados_femenino(self, obj):
        return obj._retirados_femenino


admin.site.register(Escuela, EscuelaAdmin)
admin.site.register(NivelEducativo, NivelEducativoAdmin)
admin.site.register(PeriodoEscolar)

escuela_admin.register(Escuela, EscuelaAdmin)
escuela_admin.register(NivelEducativo, NivelEducativoAdmin)
escuela_admin.register(PeriodoEscolar)
escuela_admin.register(Seccion, SeccionAdmin)
