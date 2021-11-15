# Generated by Django 3.2.9 on 2021-11-14 23:34

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0008_auto_20210523_2211'),
        ('personas', '0042_alter_estudiante_seccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='seccion',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='grado_matriculado', chained_model_field='nivel_educativo', null=True, on_delete=django.db.models.deletion.CASCADE, to='escuela.seccion', verbose_name='Sección 2021'),
        ),
    ]
