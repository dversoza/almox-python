from django.contrib import admin

from apps.core.admin import BaseAdmin

from .models import MeasurementUnit


@admin.register(MeasurementUnit)
class MeasurementUnitAdmin(BaseAdmin):
    list_display = ("name", "abbreviation", "updated_at", "updated_by")
    list_display_links = ("name",)
    search_fields = ("name", "abbreviation")
    ordering = ("name",)
    fieldsets = (("Dados", {"fields": ("name", "abbreviation")}), *BaseAdmin.fieldsets)

    def changelist_view(self, request):
        extra_context = {"title": "Unidades de Medida"}
        return super().changelist_view(request, extra_context)
