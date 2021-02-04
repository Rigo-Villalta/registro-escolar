import datetime
from tempfile import NamedTemporaryFile

from django.http import HttpResponse
from openpyxl import Workbook


def exportar_datos_de_secciones(modeladmin, request, queryset):
    """
    Acción de Django Admin que exporta a Excel las secciones con la cantidad
    de estudiantes, niños y niñas de cada sección haciendo uso de la librería
    openpyxl ver: openpyxl.readthedocs.io
    """

    wb = Workbook()
    ws = wb.active
    ws.title = "Estadísticas de secciones"
    ws.append(["Sección", "Femenino", "Masculino", "Total"])
    ws.column_dimensions["A"].width = 50.30
    ws.column_dimensions["B"].width = 9.3
    ws.column_dimensions["C"].width = 9.3
    ws.column_dimensions["D"].width = 9.3
    count = 1
    for obj in queryset:
        ws.append(
            [
                str(obj).title(),
                obj.total_femenino(),
                obj.total_masculino(),
                obj.total_estudiantes(),
            ]
        )
        count += 1

    ws.append(
        [
            "Totales",
            "=SUM(B2:B" + str(count) + ")",
            "=SUM(C2:C" + str(count) + ")",
            "=SUM(D2:D" + str(count) + ")",
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
        ] = f'attachment; filename=Cantidad_de_estudiantes_por_secciones-{datetime.datetime.now().strftime("%Y_%m_%d_%H-%M")}.xlsx'
        return response


def exportar_datos_de_grados(modeladmin, request, queryset):
    """
    Acción de Django Admin que exporta a Excel los Niveles Educativos con la
    cantidad de estudiantes, niños y niñas de cada sección haciendo uso de la
    librería openpyxl ver: openpyxl.readthedocs.io
    """

    wb = Workbook()
    ws = wb.active
    ws.title = "Estadísticas de grados"
    ws.append(["Grado", "Femenino", "Masculino", "Total"])
    ws.column_dimensions["A"].width = 50.30
    ws.column_dimensions["B"].width = 9.3
    ws.column_dimensions["C"].width = 9.3
    ws.column_dimensions["D"].width = 9.3
    count = 1
    for obj in queryset:
        ws.append(
            [
                str(obj).title(),
                obj.total_femenino(),
                obj.total_masculino(),
                obj.total_estudiantes(),
            ]
        )
        count += 1

    ws.append(
        [
            "Totales",
            "=SUM(B2:B" + str(count) + ")",
            "=SUM(C2:C" + str(count) + ")",
            "=SUM(D2:D" + str(count) + ")",
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
        ] = f'attachment; filename=Cantidad_de_estudiantes_por_grados-{datetime.datetime.now().strftime("%Y_%m_%d_%H-%M")}.xlsx'
        return response
