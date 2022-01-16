from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="created_%(class)ss"
    )
    updated_by = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="updated_%(class)ss"
    )

    class Meta:
        abstract = True
