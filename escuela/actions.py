import datetime
from tempfile import NamedTemporaryFile

from django.http import HttpResponse
from openpyxl import Workbook


def exportar_datos_de_secciones(modeladmin, request, queryset):

    wb = Workbook()
    ws = wb.active
    ws.title = "Estádisticas secciones"
    ws.append(["Sección", "Femenino", "Masculino", "Total de Estudiantes"])
    count = 0
    for obj in queryset:
        ws.append(
            [
                str(obj.__str__()),
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
        ] = f'attachment; filename=DatosPorSecciones-{datetime.datetime.now().strftime("%Y%m%d%H%M")}.xlsx'
        return response