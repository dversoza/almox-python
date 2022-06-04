from django.contrib import admin

from almox.admin.base import BaseAdmin
from .models import Person


@admin.register(Person)
class PersonAdmin(BaseAdmin):
    list_display = ("name", "is_business", "document", "phone", "stand")
    list_display_links = ("name",)
    list_filter = ("stand", "is_business", *BaseAdmin.list_filter)
    search_fields = ("name", "stand__name", "user__username")
    fieldsets = (
        (
            "Dados",
            {"fields": ("name", "is_business", "document", "phone", "stand", "user")},
        ),
        *BaseAdmin.fieldsets,
    )
