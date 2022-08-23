from rest_framework import serializers

from apps.core.serializers import BaseSerializer

from .models import MeasurementUnit, Product


class MeasurementUnitSerializer(BaseSerializer):
    class Meta:
        model = MeasurementUnit
        fields = ["id", "name", "abbreviation"]


class ProductSerializer(BaseSerializer):
    stock = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ["id", "name", "description", "measurement_unit", "stock"]

    def get_stock(self, product):
        return product.transaction_set.get_stock_for_product(product=product)
