# Generated by Django 3.1.1 on 2020-10-01 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0016_auto_20201001_0944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familia',
            name='autorizado_a_tramites',
        ),
    ]
