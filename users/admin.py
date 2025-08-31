from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin as BaseGroupAdmin
from django.utils.translation import gettext_lazy as _

from escuela.admin import escuela_admin
from .models import User, Grupo


class CustomUserAdmin(UserAdmin):
    """
    Usuario admin.
    """
    readonly_fields = ["last_login", "date_joined"]

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
escuela_admin.register(Grupo, BaseGroupAdmin)
admin.site.register(User, CustomUserAdmin)
