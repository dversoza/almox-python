from django.db import models

from almox.models import BaseModel


class MeasurementUnit(BaseModel):
    name = models.CharField(
        max_length=100, verbose_name="Nome", help_text="Nome da unidade de medida"
    )
    abbreviation = models.CharField(
        max_length=10, verbose_name="Abreviação", help_text="Ex: kg, L, m, etc."
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Unidade de Medida"
        verbose_name_plural = "Unidades de Medidas"
        ordering = ["name"]
