# Generated by Django 3.2.10 on 2021-12-28 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0002_remove_estudiante_menores_cohabitantes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EstudiantesYMenores',
        ),
    ]