from django.urls import path

from .views import index, secciones_csv, grados_csv

urlpatterns = [
    path('', index),
    path("secciones_csv", secciones_csv, name="secciones_csv" ),
    path("grados_csv", grados_csv, name="grados_csv")
]