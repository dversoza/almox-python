from django.contrib import admin

from apps.core.admin import BaseAdmin

from .models import Transaction, TransactionType


@admin.register(Transaction)
class TransactionAdmin(BaseAdmin):
    list_display = (
        "id",
        "operation",
        "type",
        "datetime",
        "stand",
        "product",
        "person",
        "quantity",
        "price",
    )
    search_fields = (
        "id",
        "operation__name",
        "type__name",
        "stand__name",
        "product__name",
        "person__name",
        "quantity",
        "price",
    )
    ordering = ("id",)
    list_display_links = ("id",)
    list_filter = (
        "datetime",
        "operation",
        "type",
        "stand",
        "product",
        "person",
        *BaseAdmin.list_filter,
    )

    fieldsets = (
        (
            "Dados",
            {
                "fields": (
                    "operation",
                    "type",
                    "datetime",
                    "stand",
                    "product",
                    "person",
                    "quantity",
                    "price",
                    "observation",
                )
            },
        ),
        *BaseAdmin.fieldsets,
    )

    def changelist_view(self, request):
        extra_context = {"title": "Movimentações"}
        return super().changelist_view(request, extra_context)


@admin.register(TransactionType)
class TransactionTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    list_display_links = ("name",)
    search_fields = ("name", "description")
    ordering = ("id",)

    def changelist_view(self, request):
        extra_context = {"title": "Tipos de Movimentação"}
        return super().changelist_view(request, extra_context)
