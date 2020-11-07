# Generated by Django 3.1.1 on 2020-10-01 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0017_remove_familia_autorizado_a_tramites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='correo_electronico',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo electrónico personal'),
        ),
        migrations.AlterField(
            model_name='responsable',
            name='correo_electronico',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo electrónico personal'),
        ),
    ]
