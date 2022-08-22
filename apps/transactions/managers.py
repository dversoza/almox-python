from django.db import models
from django.db.models import Case, F, FloatField, Sum, When


class TransactionManager(models.Manager):
    def get_stock(self, product):
        product_transactions = self.filter(product=product)
        product_transactions_with_stock = product_transactions.aggregate(
            stock=Sum(
                Case(
                    When(operation="E", then=F("quantity")),
                    When(operation="S", then=-F("quantity")),
                    output_field=FloatField(),
                )
            )
        )  # https://stackoverflow.com/questions/45506898/django-annotate-sum-of-a-column-with-filter-on-another-column
        return product_transactions_with_stock["stock"] or 0
