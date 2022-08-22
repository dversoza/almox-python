from django.contrib import admin

from apps.core.admin import BaseAdmin

from .models import Product


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
