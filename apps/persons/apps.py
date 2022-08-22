from django.apps import AppConfig


class PersonsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.persons"
    verbose_name: str = "Pessoas"
