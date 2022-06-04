from django.db import models

from almox.models import BaseModel
from measurement_units.models import MeasurementUnit


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
