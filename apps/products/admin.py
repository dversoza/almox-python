from django.contrib import admin

from apps.core.admin import BaseAdmin

from .models import MeasurementUnit, Product


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


@admin.register(Product)
class ProductAdmin(BaseAdmin):
    list_display = ("name", "measurement_unit", "description")
    list_display_links = ("name",)
    list_filter = ("measurement_unit", *BaseAdmin.list_filter)
    search_fields = ("name", "description", "measurement_unit__name")
    ordering = ("name",)
    fieldsets = (
        (
            "Dados",
            {"fields": ("name", "measurement_unit", "description")},
        ),
        *BaseAdmin.fieldsets,
    )

    def changelist_view(self, request):
        extra_context = {"title": "Produtos"}
        return super().changelist_view(request, extra_context)
