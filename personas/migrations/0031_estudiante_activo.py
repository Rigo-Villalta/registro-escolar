# Generated by Django 3.1.1 on 2020-11-13 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0030_auto_20201107_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='activo',
            field=models.BooleanField(default=True, help_text='Desmarcar si el estudiante retira documentos'),
        ),
    ]
