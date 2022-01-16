from django.db.models import CharField, BooleanField

from almox.models import BaseModel


class Stand(BaseModel):
    """
    Class that represents a stand.
    """

    name = CharField(max_length=100, unique=True, null=False)
    active = BooleanField(default=True)

    class Meta:
        verbose_name = "Stand"
        verbose_name_plural = "Stands"
        ordering = ["name"]
