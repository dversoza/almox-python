from django.contrib import admin

from almox.admin.base import BaseAdmin
from .models import Stand


@admin.register(Stand)
class StandAdmin(BaseAdmin):
    list_display = ("active", "name", "manager", "contact")
    list_display_links = ("name",)
    search_fields = ("name", "manager__name", "contact")
    ordering = ("name",)
    list_filter = ("active", "manager", *BaseAdmin.list_filter)
    fieldsets = (
        (
            "Dados",
            {"fields": ("name", "active", "manager", "contact")},
        ),
        *BaseAdmin.fieldsets,
    )

    def changelist_view(self, request):
        extra_context = {"title": "Barracas"}
        return super().changelist_view(request, extra_context)
