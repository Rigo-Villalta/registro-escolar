# Generated by Django 3.2.3 on 2021-12-28 16:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(blank=True, max_length=10, null=True, verbose_name='Código de infraestructura')),
            ],
        ),
        migrations.CreateModel(
            name='NivelEducativo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.CharField(max_length=50)),
                ('edad_normal_de_ingreso', models.PositiveSmallIntegerField(help_text='Ingrese la edad normal en que los estudiantes deben estar en este nivel educativo', validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(18)])),
            ],
            options={
                'verbose_name_plural': 'Niveles educativos.',
                'ordering': ['edad_normal_de_ingreso', 'nivel'],
            },
        ),
        migrations.CreateModel(
            name='PeriodoEscolar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese el nombre del período escolar, por ejemplo: "Año escolar 2020', max_length=50)),
                ('fecha_de_inicio', models.DateField(help_text='Ingrese la fecha de inicio del período escolar')),
                ('fecha_de_cierre', models.DateField(help_text='Ingrese la fecha de cierre del período escolar')),
            ],
            options={
                'verbose_name_plural': 'Períodos Escolares',
            },
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seccion', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='A', max_length=1, verbose_name='sección')),
                ('nivel_educativo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escuela.niveleducativo')),
                ('periodo_escolar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escuela.periodoescolar', verbose_name='período escolar')),
            ],
            options={
                'verbose_name': 'Sección',
                'verbose_name_plural': 'Secciones',
                'ordering': ('seccion',),
            },
        ),
    ]
