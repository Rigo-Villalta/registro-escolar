# Generated by Django 3.1.3 on 2020-11-23 18:31

from django.db import migrations, models
import personas.validators


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0035_auto_20201114_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menordeedad',
            name='fecha_de_nacimiento',
            field=models.DateField(blank=True, null=True, validators=[personas.validators.validate_date_is_past]),
        ),
    ]
