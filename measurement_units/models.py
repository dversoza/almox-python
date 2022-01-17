from django.db import models

from almox.models import BaseModel


class MeasurementUnit(BaseModel):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Measurement Unit"
        verbose_name_plural = "Measurement Units"
        ordering = ["name"]
