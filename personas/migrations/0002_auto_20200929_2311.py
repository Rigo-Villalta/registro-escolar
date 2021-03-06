# Generated by Django 3.1.1 on 2020-09-30 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='compania_internet',
            field=models.CharField(blank=True, choices=[('T', 'Tigo'), ('C', 'Claro'), ('J', 'Japi'), ('O', 'Otro')], help_text='Si posee internet indique la compañia.', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='hermanos',
            field=models.ManyToManyField(blank=True, help_text='Ingrese a menores de edad que vivien con el estudiante y que no son estudiantes de la institución educativa', related_name='_estudiante_hermanos_+', to='personas.Estudiante'),
        ),
    ]
