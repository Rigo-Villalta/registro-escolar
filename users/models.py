from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Usuario extendido para futuras personalizaciones
    """
    class Meta:
        db_table = "auth_user"
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"
