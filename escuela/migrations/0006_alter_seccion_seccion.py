# Generated by Django 3.2.10 on 2023-01-05 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0005_alter_niveleducativo_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seccion',
            name='seccion',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('F', 'F'), ('L', 'L'), ('M', 'M'), ('N', 'N')], default='A', max_length=1, verbose_name='sección'),
        ),
    ]
