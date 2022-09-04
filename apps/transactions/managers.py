from django.db import models
from django.db.models import Case, F, FloatField, Sum, When


class TransactionManager(models.Manager):
    def _annotate_product_stock(self, queryset):
        return queryset.values("product__name").annotate(
            stock=Sum(
                Case(
                    When(operation="E", then=F("quantity")),
                    When(operation="S", then=-F("quantity")),
                    output_field=FloatField(),
                )
            )  # https://stackoverflow.com/questions/45506898/django-annotate-sum-of-a-column-with-filter-on-another-column
        )  # https://stackoverflow.com/questions/13403609/how-to-group-by-and-aggregate-with-django

    def _annotate_stand_stock(self, queryset):
        return queryset.values("stand__name").annotate(
            stock=Sum(
                Case(
                    When(operation="E", then=F("quantity")),
                    When(operation="S", then=-F("quantity")),
                    output_field=FloatField(),
                )
            )
        )

    def get_stock_for_stand_grouped_by_product(self, stand=None):
        queryset = self.filter(stand=stand)
        queryset = self._annotate_product_stock(queryset)
        return queryset

    def get_stock_for_product_grouped_by_stand(self, product=None):
        queryset = self.filter(product=product)
        queryset = self._annotate_stand_stock(queryset)
        return queryset

    def get_stock_for_product(self, product=None):
        queryset = self.filter(product=product)
        queryset = self._annotate_product_stock(queryset)
        return queryset[0]["stock"] if queryset else 0
