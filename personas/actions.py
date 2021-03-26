import datetime
from tempfile import NamedTemporaryFile

from django.http import HttpResponse
from openpyxl import Workbook


def exportar_todos_los_datos_a_excel(self, request, queryset):
    """
    Acción de Django Admin que exporta a Excel todos los datos del modelo
    Estudiante, de todos los estudiantes en el queryset, haciendo uso de
    la librería openpyxl ver: openpyxl.readthedocs.io
    """

    meta = self.model._meta
    field_names = [field.name for field in meta.fields]

    wb = Workbook()
    ws = wb.active
    ws.title = "Estudiantes - Datos completos"

    ws.append(field_names)

    for obj in queryset:
        ws.append([str(getattr(obj, field)) for field in field_names])

    with NamedTemporaryFile() as tmp:
        wb.save(tmp.name)
        tmp.seek(0)
        stream = tmp.read()

        response = HttpResponse(
            content=stream,
            content_type="application/ms-excel",
        )
        response[
            "Content-Disposition"
        ] = f'attachment; filename=Datos_completos_de_estudiantes-{datetime.datetime.now().strftime("%Y_%m_%d_%H-%M")}.xlsx'
        return response


def exportar_datos_de_contacto_a_excel(self, request, queryset):
    """
    Acción de Django Admin que exporta a Excel datos de contacto del modelo
    Estudiante, de todos los estudiantes en el queryset, haciendo uso de
    la librería openpyxl ver: openpyxl.readthedocs.io
    """
    wb = Workbook()
    ws = wb.active
    ws.title = "Estudiantes - contactos"
    ws.append(
        [
            "Apellidos",
            "Nombres",
            "NIE",
            "Sexo",
            "Edad",
            "Sección",
            "Teléfono 1",
            "Teléfono 2",
            "Correo Electrónico",
            "Nombre de responsable",
            "Relación",
            "DUI",
            "Teléfono 1",
            "Teléfono 2",
            "Correo Electrónico",
        ]
    )
    ws.column_dimensions["A"].width = 17.60
    ws.column_dimensions["B"].width = 17.60
    ws.column_dimensions["C"].width = 10
    ws.column_dimensions["D"].width = 4.50
    ws.column_dimensions["E"].width = 4.50
    ws.column_dimensions["F"].width = 31.00
    ws.column_dimensions["G"].width = 9.4
    ws.column_dimensions["H"].width = 9.4
    ws.column_dimensions["I"].width = 29.0
    ws.column_dimensions["J"].width = 31.0
    ws.column_dimensions["K"].width = 7.25
    ws.column_dimensions["L"].width = 10.30
    ws.column_dimensions["M"].width = 9.4
    ws.column_dimensions["N"].width = 9.4
    ws.column_dimensions["O"].width = 29.0
    for obj in queryset:
        responsable = obj.responsable
        if responsable is None:
            ws.append(
                [
                    obj.apellidos,
                    obj.nombre,
                    obj.nie,
                    obj.sexo,
                    obj.edad,
                    obj.seccion.__str__().title(),
                    obj.telefono_1,
                    obj.telefono_2,
                    obj.correo_electronico,
                ]
            )
        else:
            ws.append(
                [
                    obj.apellidos,
                    obj.nombre,
                    obj.nie,
                    obj.sexo,
                    obj.edad,
                    obj.seccion.__str__().title(),
                    obj.telefono_1,
                    obj.telefono_2,
                    obj.correo_electronico,
                    f"{responsable.nombre} {responsable.apellidos}",
                    obj.get_relacion_de_responsable_display(),
                    responsable.dui,
                    responsable.telefono_1,
                    responsable.telefono_2,
                    responsable.correo_electronico,
                ]
            )

    with NamedTemporaryFile() as tmp:
        wb.save(tmp.name)
        tmp.seek(0)
        stream = tmp.read()

        response = HttpResponse(
            content=stream,
            content_type="application/ms-excel",
        )
        response[
            "Content-Disposition"
        ] = f'attachment; filename=DatosDeContactoDeEstudiantes-{datetime.datetime.now().strftime("%Y%m%d%H%M")}.xlsx'
        return response


def exportar_datos_basicos_a_excel(self, request, queryset):
    """
    Acción de Django Admin que exporta a Excel los datos básicos del modelo
    Estudiante, de todos los estudiantes en el queryset, haciendo uso de
    la librería openpyxl ver: openpyxl.readthedocs.io
    """

    wb = Workbook()
    ws = wb.active
    ws.title = "Estudiantes - Datos básicos"
    ws.append(
        [
            "Apellidos",
            "Nombres",
            "NIE",
            "Sexo",
            "Edad",
            "Sección",
            "Teléfono 1",
            "Correo Electrónico",
        ]
    )
    ws.column_dimensions["A"].width = 17.50
    ws.column_dimensions["B"].width = 19.20
    ws.column_dimensions["C"].width = 10
    ws.column_dimensions["D"].width = 4.50
    ws.column_dimensions["E"].width = 4.50
    ws.column_dimensions["F"].width = 31.00
    ws.column_dimensions["G"].width = 9.50
    ws.column_dimensions["H"].width = 40.00
    for obj in queryset:
        ws.append(
            [
                obj.apellidos,
                obj.nombre,
                obj.nie,
                obj.sexo,
                obj.edad,
                obj.seccion.__str__().title(),
                obj.telefono_1,
                obj.correo_electronico,
            ]
        )

    with NamedTemporaryFile() as tmp:
        wb.save(tmp.name)
        tmp.seek(0)
        stream = tmp.read()

        response = HttpResponse(
            content=stream,
            content_type="application/ms-excel",
        )
        response[
            "Content-Disposition"
        ] = f'attachment; filename=ListaDeEstudiantes-{datetime.datetime.now().strftime("%Y%m%d%H%M")}.xlsx'
        return response