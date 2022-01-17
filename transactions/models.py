from django.contrib.auth.models import User
from django.db import models

from almox.models import BaseModel
from persons.models import Person
from products.models import Product
from stands.models import Stand


class Transaction(BaseModel):
    OPERATIONS = [("E", "Entrada"), ("S", "Saida")]
    TYPES = [("I", "Interna"), ("C", "Compra"), ("D", "Doação"), ("R", "Devolução")]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stand = models.ForeignKey(Stand, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    operation = models.CharField(max_length=1, choices=OPERATIONS, default="S")
    type = models.CharField(max_length=1, choices=TYPES, default="I")
    quantity = models.FloatField()
    price = models.FloatField()
    observation = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
        ordering = ["-created_at"]
