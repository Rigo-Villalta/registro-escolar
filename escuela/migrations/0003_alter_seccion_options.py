# Generated by Django 3.2.10 on 2022-01-06 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0002_periodoescolar_periodo_activo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seccion',
            options={'ordering': ['nivel_educativo__edad_normal_de_ingreso', 'nivel_educativo', 'seccion'], 'verbose_name': 'Sección', 'verbose_name_plural': 'Secciones'},
        ),
    ]
