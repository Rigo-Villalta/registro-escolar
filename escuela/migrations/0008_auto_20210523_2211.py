# Generated by Django 3.2.3 on 2021-05-24 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0007_auto_20201107_1408'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='niveleducativo',
            options={'ordering': ['edad_normal_de_ingreso', 'nivel'], 'verbose_name_plural': 'Niveles educativos.'},
        ),
        migrations.AlterModelOptions(
            name='seccion',
            options={'ordering': ('seccion',), 'verbose_name': 'Sección', 'verbose_name_plural': 'Secciones'},
        ),
    ]