from django.contrib.auth.models import User
from django.db import models

from almox.models import BaseModel


class Person(BaseModel):
    """
    Model for persons.
    """

    name = models.CharField(max_length=100)
    is_business = models.BooleanField(default=False)
    document = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    stand = models.ForeignKey(
        "stands.Stand", on_delete=models.CASCADE, related_name="staff", null=True
    )
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Person"
        verbose_name_plural = "Persons"
