from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")
    created_by = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="created_%(class)ss",
        verbose_name="Criado por",
    )
    updated_by = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="updated_%(class)ss",
        null=True,
        verbose_name="Atualizado por",
    )

    class Meta:
        abstract = True
