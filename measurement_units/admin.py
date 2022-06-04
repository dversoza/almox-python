from django.contrib import admin

from almox.admin.base import BaseAdmin
from .models import MeasurementUnit


@admin.register(MeasurementUnit)
class MeasurementUnitAdmin(BaseAdmin):
    list_display = ("name", "abbreviation", "updated_at", "updated_by")
    list_display_links = ("name",)
    search_fields = ("name", "abbreviation")
    ordering = ("name",)
    fieldsets = (("Dados", {"fields": ("name", "abbreviation")}), *BaseAdmin.fieldsets)
