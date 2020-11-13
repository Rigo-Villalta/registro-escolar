import codecs
import csv

from django.http import HttpResponse


class ExportCsvMixin:

    def exportar_a_excel(self, request, queryset):
        meta = self.model._meta
        try:
            self.csv_fields
            field_names = self.csv_fields
        except AttributeError:
            field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(
            meta)
        writer = csv.writer(response)

        response.write(codecs.BOM_UTF8)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field)
                                  for field in field_names])

        return response

    def exportar_a_excel_basico(self, request, queryset):
        meta = self.model._meta
        try:
            self.csv_fields
            field_names = ["nombre", "apellidos", "seccion"]
        except AttributeError:
            field_names = ["nombre", "apellidos", "seccion", "nie", "sexo"]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        response.write(codecs.BOM_UTF8)
        writer.writerow(["nombre", "apellidos", "sección", "nie", "sexo"])
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        
        return response
    exportar_a_excel_basico.short_description = "Exportar a excel básico"
