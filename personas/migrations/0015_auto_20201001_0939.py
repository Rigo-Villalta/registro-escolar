# Generated by Django 3.1.1 on 2020-10-01 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0014_familia_autorizado_a_tramites'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudiante',
            old_name='responsable',
            new_name='familiares',
        ),
        migrations.RemoveField(
            model_name='familia',
            name='responsable',
        ),
        migrations.AddField(
            model_name='familia',
            name='familiar',
            field=models.ForeignKey(default=1, help_text='Selecciones un familiar para el estudiante', on_delete=django.db.models.deletion.CASCADE, to='personas.responsable'),
            preserve_default=False,
        ),
    ]
