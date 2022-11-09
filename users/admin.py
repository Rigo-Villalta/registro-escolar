from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from escuela.admin import escuela_admin
from .models import User


class CustomUserAdmin(UserAdmin):
    """
    Usuario admin.
    """

    fieldsets = (
        (_("user"), {"fields": ("username", "password", "is_active", "is_staff")}),
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
                    "is_staff",
                    "first_name",
                    "last_name",
                    "tipo_de_usuario",
                ),
            },
        ),
    )

    list_display = ("username", "email", "last_name", "first_name", "tipo_de_usuario")
    readonly_fields = ("last_login", "date_joined")
    list_filter = ["tipo_de_usuario", "is_active"]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions
    
    def get_queryset(self, request):
        active_filter = request.GET.get("is_active__exact")
        if active_filter:
            return super().get_queryset(request)
        return super().get_queryset(request).filter(is_active=True)


escuela_admin.register(User, CustomUserAdmin)
admin.site.register(User, CustomUserAdmin)
