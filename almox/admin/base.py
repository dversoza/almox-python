from django.contrib import admin

admin.site.site_header = "Gerenciamento de informação do Almoxarifado"
admin.site.site_title = "Almox Admin"
admin.site.index_title = "Almox Admin"


class BaseAdmin(admin.ModelAdmin):
    list_per_page = 25
    list_filter = ("created_at", "updated_at", "created_by", "updated_by")
    ordering = ("-updated_at", "-created_at")
    date_hierarchy = "updated_at"
    readonly_fields = ("created_at", "updated_at", "created_by", "updated_by")
    fieldsets: tuple = (
        (
            "Outros",
            {"fields": ("created_at", "updated_at", "created_by", "updated_by")},
        ),
    )
    save_as = True
    actions_on_top: bool = False
    actions_on_bottom = True
    actions_selection_counter = True

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()
