# Generated by Django 3.1.1 on 2020-10-01 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0019_auto_20201001_1035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='municipio',
        ),
        migrations.AddField(
            model_name='estudiante',
            name='municipio_de_nacimiento',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='personas.municipio'),
        ),
    ]
