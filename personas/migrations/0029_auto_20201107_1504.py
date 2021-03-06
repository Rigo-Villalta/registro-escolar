# Generated by Django 3.1.1 on 2020-11-07 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0028_auto_20201107_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='cantidad_cohabitantes',
            field=models.PositiveSmallIntegerField(help_text='Indique la cantidad de personas que vivien con el estudiante'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='etnia',
            field=models.CharField(choices=[('N', 'Ninguna'), ('K', 'Kakawira'), ('L', 'Lenca'), ('N', 'Nahuat-Pipil')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='seccion_previa',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], help_text='Solo si estudió en esta institución(CEDHRA) el año escolar anterior', max_length=1),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='tipo_de_sangre',
            field=models.CharField(blank=True, choices=[('A+', 'A Rh positivo(A rh+)'), ('A-', 'A Rh negativo(A rh-)'), ('B+', 'B Rh positivo(B rh+)'), ('B-', 'B Rh negativo(B rh-)'), ('O+', 'O Rh positivo(O rh+)'), ('O-', 'O Rh negativo(O rh-)'), ('AB+', 'AB Rh positivo(AB rh+)'), ('AB-', 'AB Rh negativo(AB rh-)')], max_length=3),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='utiliza_transporte_publico',
            field=models.BooleanField(verbose_name='Utiliza transporte público'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='utiliza_vehiculo',
            field=models.BooleanField(verbose_name='Utiliza Vehículo'),
        ),
        migrations.AlterField(
            model_name='menordeedad',
            name='medio_de_transporte',
            field=models.CharField(blank=True, choices=[('B', 'Bicicleta'), ('V', 'Vehículo'), ('P', 'Transpote Público'), ('E', 'Transporte Escolar'), ('M', 'Motocicleta'), ('C', 'Camina'), ('O', 'Otro')], help_text='Medio de transporte principal del menor', max_length=1, null=True),
        ),
    ]
