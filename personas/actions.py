import datetime
from tempfile import NamedTemporaryFile

from django.http import HttpResponse
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill


def set_border(ws, cell_range):
    thin = Side(border_style="thin", color="000000")
    for row in ws[cell_range]:
        for cell in row:
            cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)


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
        ] = f'attachment; filename=DatosDeContactoDeEstudiantes-{datetime.datetime.now().strftime("%Y_%m_%d-%H%M")}.xlsx'
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
        ] = f'attachment; filename=ListaDeEstudiantes-{datetime.datetime.now().strftime("%Y_%m_%d-%H%M")}.xlsx'
        return response


def exportar_a_excel_datos_completos_de_responsables(self, request, queryset):
    """
    Acción que toma un queryset de Responsable y exporta
    a excel las columnas: Nombre, Apellidos, DUI, Sexo, Fecha de nacimiento,
    teléfono 1 y 2, correo electrónico, Situación laboral, Dirección
    y observaciones, haciendo uso de
    la librería openpyxl ver: openpyxl.readthedocs.io
    """
    wb = Workbook()
    ws = wb.active
    ws.title = "Responsables - Estudiantes"
    ws.append(
        [
            "Apellidos",
            "Nombre",
            "DUI",
            "Sexo",
            "Nacimiento",
            "Teléfono 1",
            "Teléfono 2",
            "Correo Electrónico",
            "Situación Laboral",
            "Dirección",
            "Observaciones",
        ]
    )
    ws.column_dimensions["A"].width = 20
    ws.column_dimensions["B"].width = 20
    ws.column_dimensions["C"].width = 11
    ws.column_dimensions["D"].width = 9
    ws.column_dimensions["E"].width = 11
    ws.column_dimensions["F"].width = 10
    ws.column_dimensions["G"].width = 10
    ws.column_dimensions["H"].width = 30
    ws.column_dimensions["I"].width = 16
    ws.column_dimensions["J"].width = 65
    ws.column_dimensions["K"].width = 65
    for obj in queryset:
        ws.append(
            [
                obj.apellidos,
                obj.nombre,
                obj.dui,
                obj.get_sexo_display(),
                obj.fecha_de_nacimiento,
                obj.telefono_1,
                obj.telefono_2,
                obj.correo_electronico,
                obj.get_situacion_laboral_display(),
                obj.direccion_de_residencia,
                obj.observaciones,
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
        ] = f'attachment; filename=ListaDeResponsables-{datetime.datetime.now().strftime("%Y_%m_%d-%H%M")}.xlsx'
        return response


def exportar_a_excel_estudiantes_y_responsables_por_familia_y_seccion(
    self, request, queryset
):
    """
    Acción que toma un queryset de Estudiantes y exporta
    a excel las columnas: Responsable, DUI de responsable,
    estudiante y sección del estudiante, ordenados en primer
    lugar por sección, pero con familias en conjunto, es decir
    el primer niño de kinder 3 es el primero, si tiene hermanos
    luego ellos, luego el segundo niño de kinder 3 y sus hermanos y así
    sucesivamente, estos hermanos ya no aparecen en su repectiva seccion
    haciemos uso de la librería openpyxl ver: openpyxl.readthedocs.io
    """

    # optimización del queryset para los datos
    # de responsable relacionados y ordenados
    # para ello pasamos el query a values
    estudiantes = (
        queryset.select_related("responsable")
        .order_by("grado_matriculado", "seccion", "apellidos", "nombre")
        .values(
            "responsable__id",
            "responsable__apellidos",
            "responsable__nombre",
            "responsable__dui",
            "apellidos",
            "nombre",
            "grado_matriculado__nivel",
            "seccion__seccion",
        )
    )
    wb = Workbook()
    ws = wb.active
    ws.title = "Responsables - Estudiantes"
    ws.append(["Responsable", "DUI de responsable", "Estudiante", "Sección"])
    ws.column_dimensions["A"].width = 35
    ws.column_dimensions["B"].width = 12
    ws.column_dimensions["C"].width = 35
    ws.column_dimensions["D"].width = 45

    # el algoritmo para encontrar otros estudiantes del mismo
    # responsable se hace a nivel de Python y no ORM
    responsables_usados = []
    count = 0
    for estudiante in estudiantes:
        if estudiante["responsable__id"] in responsables_usados:
            count += 1
        else:
            ws.append(
                [
                    f"{estudiante['responsable__apellidos']}, {estudiante['responsable__nombre']}",
                    estudiante["responsable__dui"],
                    f"{estudiante['apellidos']}, {estudiante['nombre']}",
                    f"{estudiante['grado_matriculado__nivel']} - {estudiante['seccion__seccion']}",
                ]
            )
            for estudiante_b in estudiantes[count + 1 :]:
                if estudiante["responsable__id"] == estudiante_b["responsable__id"]:
                    ws.append(
                        [
                            f"{estudiante_b['responsable__apellidos']}, {estudiante_b['responsable__nombre']}",
                            estudiante_b["responsable__dui"],
                            f"{estudiante_b['apellidos']}, {estudiante_b['nombre']}",
                            f"{estudiante_b['grado_matriculado__nivel']} - {estudiante_b['seccion__seccion']}",
                        ]
                    )
            responsables_usados.append(estudiante["responsable__id"])
            count += 1

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
        ] = f'attachment; filename=ListaDeEstudiantesYResponsables-{datetime.datetime.now().strftime("%Y_%m_%d-%H%M")}.xlsx'
        return response


def exportar_a_excel_estudiantes_y_responsables_por_seccion(self, request, queryset):
    """
    Acción que toma un queryset de Estudiantes y exporta
    a excel las columnas: Responsable, DUI de responsable,
    estudiante y sección del estudiante ordenados por seccion,
    haciendo uso de la librería openpyxl ver: openpyxl.readthedocs.io
    """

    # optimización del queryset para los datos
    # de responsable relacionados y ordenados
    # para ello pasamos el query a values
    estudiantes = (
        queryset.select_related("responsable")
        .order_by("grado_matriculado", "seccion", "apellidos", "nombre")
        .values(
            "responsable__id",
            "responsable__apellidos",
            "responsable__nombre",
            "responsable__dui",
            "apellidos",
            "nombre",
            "grado_matriculado__nivel",
            "seccion__seccion",
        )
    )
    wb = Workbook()
    ws = wb.active
    ws.title = "Responsables - Estudiantes"
    ws.append(["Responsable", "DUI de responsable", "Estudiante", "Sección"])
    ws.column_dimensions["A"].width = 35
    ws.column_dimensions["B"].width = 12
    ws.column_dimensions["C"].width = 35
    ws.column_dimensions["D"].width = 45

    # utilizamos los values
    for estudiante in estudiantes:
        ws.append(
            [
                f"{estudiante['responsable__apellidos']}, {estudiante['responsable__nombre']}",
                estudiante["responsable__dui"],
                f"{estudiante['apellidos']}, {estudiante['nombre']}",
                f"{estudiante['grado_matriculado__nivel']} - {estudiante['seccion__seccion']}",
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
        ] = f'attachment; filename=ListaDeEstudiantesYResponsables-{datetime.datetime.now().strftime("%Y_%m_%d-%H%M")}.xlsx'
        return response


def exportar_a_excel_lista_de_firmas_por_seccion_y_familia(self, request, queryset):
    """
    Acción que toma un queryset de Estudiantes y exporta
    a excel las columnas: Responsable, DUI de responsable,
    estudiante y sección del estudiante, ordenados en primer
    lugar por sección, pero con familias en conjunto, es decir
    el primer niño de kinder 3 es el primero, si tiene hermanos
    luego ellos, luego el segundo niño de kinder 3 y sus hermanos y así
    sucesivamente, estos hermanos ya no aparecen en su repectiva seccion
    haciemos uso de la librería openpyxl ver: openpyxl.readthedocs.io
    """

    # optimización del queryset para los datos
    # de responsable relacionados y ordenados
    # para ello pasamos el query a values

    estudiantes = (
        queryset.prefetch_related("grado_matriculado__nivel")
        .order_by("grado_matriculado", "seccion", "apellidos", "nombre")
        .values(
            "responsable__id",
            "responsable__apellidos",
            "responsable__nombre",
            "responsable__dui",
            "apellidos",
            "nombre",
            "grado_matriculado__nivel",
            "seccion__id",
            "seccion__seccion",
        )
    )

    wb = Workbook()

    responsables_usados = []
    count = 0
    seccion_actual = "0"
    counter_interno = 1
    ws = None
    for estudiante in estudiantes:
        if estudiante["responsable__id"] in responsables_usados:
            count += 1
        else:
            if estudiante["seccion__id"] != seccion_actual:
                if ws is not None:
                    set_border(ws, "A7:F" + str(counter_interno + 6))
                    for row in range(8, counter_interno + 7):
                        rd = ws.row_dimensions[row]
                        rd.height = 25
                        a = ws["A" + str(row)]
                        a.alignment = Alignment(horizontal="center")
                ws = wb.create_sheet(
                    f"{estudiante['grado_matriculado__nivel']}{estudiante['seccion__seccion']}"
                )
                ws.title = (
                    f"{estudiante['grado_matriculado__nivel']} {estudiante['seccion__seccion']}".title()
                    .replace(" ", "")
                    .replace("Años", "")
                    .replace("Año", "")
                    .replace("Bachillerato", "")
                )
                ws.column_dimensions["A"].width = 3
                ws.column_dimensions["B"].width = 36
                ws.column_dimensions["C"].width = 11
                ws.column_dimensions["D"].width = 36
                ws.column_dimensions["E"].width = 40
                ws.column_dimensions["F"].width = 20
                ws["A1"] = 'Complejo Educativo "Dr. Humberto Romero Alvergue"'
                bold = Font(bold=True)
                a1 = ws["A1"]
                a1.font = bold
                a1.alignment = Alignment(horizontal="center")
                ws.merge_cells("A1:F1")
                ws["A2"] = "Código de Infraestructura 11674"
                a2 = ws["A2"]
                a2.font = bold
                a2.alignment = Alignment(horizontal="center")
                ws.merge_cells("A2:F2")
                ws["A3"] = "Descripción de actividad"
                ws.merge_cells("A3:F3")
                ws["A4"] = "Fecha de entrega"
                ws.merge_cells("A4:F4")
                ws["A5"] = "Se recibe"
                ws.merge_cells("A5:F5")
                ws["A6"] = ""
                ws.merge_cells("A6:F6")
                ws.append(
                    [
                        "Nº",
                        "Nombre de Padre /Madre o Responsable",
                        "Nº de DUI",
                        "Estudiante",
                        "Sección de estudiante",
                        "Firma",
                    ]
                )
                counter_interno = 1
                a7 = ws["A7"]
                b7 = ws["B7"]
                c7 = ws["C7"]
                d7 = ws["D7"]
                e7 = ws["E7"]
                f7 = ws["F7"]
                fill_gray = PatternFill(
                    fill_type="solid", start_color="DDDDDD", end_color="DDDDDD"
                )
                a7.fill = fill_gray
                b7.fill = fill_gray
                c7.fill = fill_gray
                d7.fill = fill_gray
                e7.fill = fill_gray
                f7.fill = fill_gray
            ws.append(
                [
                    str(counter_interno),
                    f"{estudiante['responsable__apellidos']}, {estudiante['responsable__nombre']}",
                    estudiante["responsable__dui"],
                    f"{estudiante['apellidos']}, {estudiante['nombre']}",
                    f"{estudiante['grado_matriculado__nivel'].title()} {estudiante['seccion__seccion']}",
                ]
            )
            counter_interno += 1
            for estudiante_b in estudiantes[count + 1 :]:
                if estudiante["responsable__id"] == estudiante_b["responsable__id"]:
                    ws.append(
                        [
                            str(counter_interno),
                            f"{estudiante_b['responsable__apellidos']}, {estudiante_b['responsable__nombre']}",
                            estudiante_b["responsable__dui"],
                            f"{estudiante_b['apellidos']}, {estudiante_b['nombre']}",
                            f"{estudiante_b['grado_matriculado__nivel'].title()} {estudiante_b['seccion__seccion']}",
                        ]
                    )
                    counter_interno += 1
            seccion_actual = estudiante["seccion__id"]
            responsables_usados.append(estudiante["responsable__id"])
            count += 1

    set_border(ws, "A7:F" + str(counter_interno + 6))
    for row in range(8, counter_interno + 7):
        rd = ws.row_dimensions[row]
        rd.height = 25
        a = ws["A" + str(row)]
        a.alignment = Alignment(horizontal="center")
    del wb["Sheet"]

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
        ] = f'attachment; filename=ListaDeEstudiantesYResponsablesParaFirmas-{datetime.datetime.now().strftime("%Y_%m_%d-%H%M")}.xlsx'
        return response
