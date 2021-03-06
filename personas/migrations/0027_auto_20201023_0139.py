# Generated by Django 3.1.1 on 2020-10-23 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0026_auto_20201023_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='medicamentos',
            field=models.CharField(blank=True, max_length=200, verbose_name='Escriba el nombre de los medicamentos'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='tipo_de_sangre',
            field=models.CharField(blank=True, choices=[('A+', 'A positivo(A+)'), ('A-', 'A negativo(A-)'), ('B+', 'B positivo(B+)'), ('B-', 'B negativo(B-)'), ('O+', 'O positivo(O+)'), ('O-', 'O negativo(O-)'), ('AB+', 'AB positivo(AB+)'), ('AB-', 'AB negativo(AB-)')], max_length=3),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='usa_medicamentos',
            field=models.BooleanField(default=False, verbose_name='¿El estudiante toma algún medicamento prescrito permanentemente?'),
        ),
        migrations.AddField(
            model_name='responsable',
            name='direccion_de_residencia',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='responsable',
            name='situacion_laboral',
            field=models.CharField(choices=[('E', 'Empleado'), ('D', 'Desempleado'), ('I', 'Empleo Informal'), ('A', 'Ama de Casa'), ('M', 'Empresario'), ('P', 'Profesional autónomo')], default='D', max_length=20, verbose_name='Situación Laboral'),
        ),
    ]
