from django.db import models

from apps.core.models import BaseModel
from apps.persons.models import Person
from apps.products.models import Product
from apps.stands.models import Stand

from .managers import TransactionManager


OPERATIONS = [("E", "Entrada"), ("S", "Saida")]


class TransactionType(BaseModel):
    operation = models.CharField(
        max_length=1,
        choices=OPERATIONS,
        verbose_name="Operação",
        help_text="Entrada: produtos entrando no almoxarifado<br>Saída: produtos saindo do almoxarifado",
    )
    name = models.CharField(
        max_length=100, unique=True, null=False, verbose_name="Nome"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descrição",
        max_length=500,
        help_text="Descrição do tipo de movimentação",
    )

    default_from_stand = models.ForeignKey(
        Stand,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="default_to_stand",
        verbose_name='Padrão para campo "De:"',
        help_text="Barraca padrão para executar este tipo de movimentação",
    )
    default_to_stand = models.ForeignKey(
        Stand,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="default_from_stand",
        verbose_name='Padrão para campo "Para:"',
        help_text="Barraca padrão para receber este tipo de movimentação",
    )

    class Meta:
        verbose_name = "Tipo de movimentação"
        verbose_name_plural = "Tipos de movimentação"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return f"<TransactionType({self.id}): {self.name}>"


class Transaction(BaseModel):
    datetime = models.DateTimeField(
        null=False,
        verbose_name="Data e Hora",
        help_text="Data e hora da movimentação",
    )
    # TO BE DELETED
    stand = models.ForeignKey(
        Stand, on_delete=models.CASCADE, verbose_name="Barraca", null=True, blank=True
    )
    from_stand = models.ForeignKey(
        Stand, on_delete=models.CASCADE, verbose_name="De", related_name="from_stand"
    )
    to_stand = models.ForeignKey(
        Stand, on_delete=models.CASCADE, verbose_name="Para", related_name="to_stand"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Produto"
    )
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        verbose_name="Pessoa",
        help_text="Pessoa responsável pela movimentação",
    )
    operation = models.CharField(
        max_length=1,
        choices=OPERATIONS,
        default="S",
        verbose_name="Operação",
        help_text="Entrada: produtos entrando no almoxarifado<br>Saída: produtos saindo do almoxarifado",
    )
    type = models.ForeignKey(
        TransactionType, on_delete=models.PROTECT, verbose_name="Tipo"
    )
    quantity = models.FloatField(verbose_name="Quantidade")
    price = models.IntegerField(
        verbose_name="Preço",
        help_text="Valor global da movimentação <b>em centavos</b>; 0 (zero) para saídas internas e devoluções",
    )
    details = models.TextField(blank=True, null=True, verbose_name="Observações")

    objects = TransactionManager()

    class Meta:
        verbose_name = "Movimentação"
        verbose_name_plural = "Movimentações"
        ordering = ["-created_at", "-updated_at"]

    def __str__(self):
        return f"{int(self.quantity)} {self.product.measurement_unit.abbreviation} de {self.product.name} para a Barraca {self.stand.name}"

    def __repr__(self) -> str:
        return f"<Transaction({self.id}): {self.product.name}>"
