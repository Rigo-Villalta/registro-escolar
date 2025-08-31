from django.contrib.auth.models import AbstractUser, Group


class User(AbstractUser):
    """
    Usuario extendido para futuras personalizaciones
    """
    class Meta:
        db_table = "auth_user"
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"


class Grupo(Group):
    """
    Modelo Proxy para poder ser visto en el admin
    """
    class Meta:
    
        proxy = True
        verbose_name = "grupo de usuarios"
        verbose_name_plural = "grupos de usuarios"