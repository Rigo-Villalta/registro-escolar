# Generated by Django 3.1.1 on 2020-09-30 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(blank=True, max_length=10, null=True, verbose_name='Código de infraestructura')),
            ],
        ),
        migrations.CreateModel(
            name='NivelEducativo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.CharField(max_length=50)),
                ('edad_normal', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seccion', models.CharField(max_length=1, verbose_name='sección')),
                ('nivel_educativo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escuela.niveleducativo')),
            ],
        ),
    ]
