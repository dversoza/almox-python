from django.db import models

from almox.models import BaseModel
from persons.models import Person


class Stand(BaseModel):
    """
    Class that represents a stand.
    """

    name = models.CharField(max_length=100, unique=True, null=False)
    active = models.BooleanField(default=True)
    contact = models.CharField(max_length=100, null=True)
    manager = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name="stand_manager", null=True
    )

    class Meta:
        verbose_name = "Stand"
        verbose_name_plural = "Stands"
        ordering = ["name"]

    def __str__(self):
        return self.name
