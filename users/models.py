from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    TIPOS_DE_USUARIO = (
        (1, "Administrador"),
        (2, "Profesor"),
        (3, "Digitador")
    )
    tipo_de_usuario = models.PositiveSmallIntegerField(
        choices=TIPOS_DE_USUARIO,
        default=3
    )
    
    class Meta:
        db_table='auth_user'
        verbose_name= "usuario"