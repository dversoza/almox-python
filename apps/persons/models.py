from django.contrib.auth.models import User
from django.db import models

from apps.core.models import BaseModel


class Person(BaseModel):
    """
    Model for persons.
    """

    name = models.CharField(max_length=100, verbose_name="Nome")
    is_business = models.BooleanField(
        default=False,
        verbose_name="Pessoa Jurídica",
        help_text="Marque se a pessoa é uma empresa.",
    )
    document = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="CPF/CNPJ"
    )
    phone = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="Telefone"
    )
    stand = models.ForeignKey(
        "stands.Stand",
        on_delete=models.CASCADE,
        related_name="staff",
        verbose_name="Barraca",
        null=True,
        blank=True,
        help_text="Selecione a barraca em que a pessoa trabalha.",
    )
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name="Usuário",
        related_name="person",
    )
    active = models.BooleanField(default=True, verbose_name="Ativo")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
        ordering = ["name"]
