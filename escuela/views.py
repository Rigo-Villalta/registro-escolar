import csv
import codecs
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import NivelEducativo, Seccion

def index(request):
    return redirect('admin:index')


def secciones_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    secciones = Seccion.objects.all()

    response.write(codecs.BOM_UTF8)
    writer = csv.writer(response)
    writer.writerow(['Nivel Educativo', 'Sección', 'Femenino', 'Masculino', 'Estudiantes'])
    for obj in secciones:
            writer.writerow([obj.nivel_educativo, obj.seccion, obj.femenino(), obj.masculino(), obj.estudiantes()])

    return response


def grados_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    grados = NivelEducativo.objects.all()

    writer = csv.writer(response)
    writer.writerow(['Grado', 'Femenino', 'Masculino', 'Estudiantes'])
    for obj in grados:
            writer.writerow([obj.nivel, obj.femenino(), obj.masculino(), obj.estudiantes()])

    return response