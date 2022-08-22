from django.db import models
from django.db.models import Case, F, FloatField, Sum, When


class TransactionManager(models.Manager):
    def _annotate_stock(self, queryset):
        return queryset.values("product__name").annotate(
            stock=Sum(
                Case(
                    When(operation="E", then=F("quantity")),
                    When(operation="S", then=-F("quantity")),
                    output_field=FloatField(),
                )
            )  # https://stackoverflow.com/questions/45506898/django-annotate-sum-of-a-column-with-filter-on-another-column
        )  # https://stackoverflow.com/questions/13403609/how-to-group-by-and-aggregate-with-django

    def get_stock_for_stand(self, stand=None):
        queryset = self.filter(stand=stand)
        queryset = self._annotate_stock(queryset)
        return queryset

    def get_stock_for_product(self, product=None):
        queryset = self.filter(product=product)
        queryset = self._annotate_stock(queryset)
        return queryset[0]["stock"] if queryset else 0
