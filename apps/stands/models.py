from django.db import models

from apps.core.models import BaseModel
from apps.persons.models import Person


class Stand(BaseModel):
    """
    Class that represents a stand.
    """

    name = models.CharField(
        max_length=100, unique=True, null=False, verbose_name="Nome"
    )
    active = models.BooleanField(default=True, verbose_name="Ativa")
    contact = models.CharField(
        max_length=100,
        null=True,
        verbose_name="Contato",
        help_text="Telefone ou celular do responsável pela barraca",
    )
    manager = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="stand_manager",
        null=True,
        verbose_name="Responsável",
        help_text="Responsável pela barraca",
    )

    class Meta:
        verbose_name = "Barraca"
        verbose_name_plural = "Barracas"
        ordering = ["name"]

    def __str__(self):
        return self.name
