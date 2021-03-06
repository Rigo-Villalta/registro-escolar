# Generated by Django 3.1.1 on 2020-11-07 20:52

from django.db import migrations, models
import django.db.models.deletion
import personas.validators


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0007_auto_20201107_1408'),
        ('personas', '0027_auto_20201023_0139'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menordeedad',
            options={'verbose_name': ' Menor de edad', 'verbose_name_plural': 'Menores de edad'},
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='down',
            field=models.BooleanField(default=False, verbose_name='Síndrome de Down'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='seccion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='escuela.seccion', verbose_name='Sección'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='seccion_previa',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], help_text='Solo si estudio en esta institución(CEDHRA)', max_length=1),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='tipo_de_sangre',
            field=models.CharField(blank=True, choices=[('A+', 'A Rh positivo(A rh+)'), ('A-', 'A Rh negativo(A-)'), ('B+', 'B Rh positivo(B+)'), ('B-', 'B Rh negativo(B-)'), ('O+', 'O Rh positivo(O+)'), ('O-', 'O Rh negativo(O-)'), ('AB+', 'AB Rh positivo(AB+)'), ('AB-', 'AB Rh negativo(AB-)')], max_length=3),
        ),
        migrations.AlterField(
            model_name='menordeedad',
            name='fecha_de_nacimiento',
            field=models.DateField(validators=[personas.validators.validate_date_is_past]),
        ),
        migrations.AlterField(
            model_name='responsable',
            name='dui',
            field=models.CharField(max_length=12, unique=True, verbose_name='DUI'),
        ),
    ]
