# Generated by Django 3.2.10 on 2021-12-28 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_tipo_de_usuario'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'usuario'},
        ),
    ]