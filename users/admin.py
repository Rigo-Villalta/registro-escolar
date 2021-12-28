from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


@register(User)
class CustomUserAdmin(UserAdmin):
    """
    Usuario admin.
    """

    fieldsets = (
        (_("user"), {"fields": ("username", "password", "is_active")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "tipo_de_usuario",
                    "email",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                    "tipo_de_usuario",
                ),
            },
        ),
    )

    list_display = (
        "username",
        "email",
        "last_name",
        "first_name",
    )

    def get_readonly_fields(self, request, obj=None):
        if obj is None:
            return ("last_login", "date_joined")
        else:
            return ("last_login", "date_joined", "user_type")
