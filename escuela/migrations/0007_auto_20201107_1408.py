# Generated by Django 3.1.1 on 2020-11-07 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0006_auto_20201107_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seccion',
            name='periodo_escolar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escuela.periodoescolar', verbose_name='período escolar'),
        ),
    ]
