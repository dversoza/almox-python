from django.db import models

from apps.core.models import BaseModel


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


class Product(BaseModel):
    name = models.CharField("Nome", max_length=100, unique=True)
    description = models.TextField(
        "Descrição", blank=True, help_text="Descrição do produto"
    )
    measurement_unit = models.ForeignKey(
        MeasurementUnit, on_delete=models.PROTECT, verbose_name="Unidade de Medida"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["name"]
