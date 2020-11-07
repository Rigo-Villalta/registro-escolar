# Generated by Django 3.1.1 on 2020-10-01 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0020_auto_20201001_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='municipio_de_residencia',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reside_en', to='personas.municipio'),
        ),
    ]
