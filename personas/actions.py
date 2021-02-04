import codecs
import csv
import datetime
from tempfile import NamedTemporaryFile

from django.http import HttpResponse
from openpyxl import Workbook


def exportar_a_excel_completo(self, request, queryset):
    meta = self.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attachment; filename={}.csv".format(meta)
    writer = csv.writer(response)

    response.write(codecs.BOM_UTF8)
    writer.writerow(field_names)
    for obj in queryset:
        row = writer.writerow([getattr(obj, field) for field in field_names])

    return response


def exportar_todos_los_datos_a_excel(self, request, queryset):
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
        ] = f'attachment; filename=DatosCompletosDeEstudiantes-{datetime.datetime.now().strftime("%Y%m%d%H%M")}.xlsx'
        return response


def exportar_datos_de_contacto_a_excel(self, request, queryset):

    wb = Workbook()
    ws = wb.active
    ws.title = "Estudiantes - contactos"
    ws.append(
        [
            "Apellidos",
            "Nombres",
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
    for obj in queryset:
        responsable = obj.responsable
        if responsable is None:
            ws.append(
                [
                    obj.apellidos,
                    obj.nombre,
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
                    obj.sexo,
                    obj.edad,
                    obj.seccion.__str__().title(),
                    obj.telefono_1,
                    obj.telefono_2,
                    obj.correo_electronico,
                    responsable.__str__(),
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

    wb = Workbook()
    ws = wb.active
    ws.title = "Estudiantes - Datos básicos"
    ws.append(
        [
            "Apellidos",
            "Nombres",
            "Sexo",
            "Edad",
            "Sección",
            "Teléfono 1",
            "Correo Electrónico",
        ]
    )
    for obj in queryset:
        ws.append(
            [
                obj.apellidos,
                obj.nombre,
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