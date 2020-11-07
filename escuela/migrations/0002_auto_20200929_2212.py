# Generated by Django 3.1.1 on 2020-09-30 04:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='niveleducativo',
            name='edad_normal',
        ),
        migrations.AddField(
            model_name='niveleducativo',
            name='edad_normal_de_ingreso',
            field=models.PositiveSmallIntegerField(default=3, help_text='Ingrese la edad normal en que los estudiantes deben estar en este nivel educativo', validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(18)]),
            preserve_default=False,
        ),
    ]
