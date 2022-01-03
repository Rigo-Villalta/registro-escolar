# Generated by Django 3.2.10 on 2022-01-03 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0002_periodoescolar_periodo_activo'),
        ('personas', '0007_auto_20220102_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='seccion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='escuela.seccion', verbose_name='Sección'),
        ),
    ]
