from rest_framework import serializers

from apps.core.serializers import BaseSerializer

from .models import MeasurementUnit, Product


class MeasurementUnitSerializer(BaseSerializer):
    class Meta:
        model = MeasurementUnit
        fields = ["id", "name", "abbreviation"]


class ProductSerializer(BaseSerializer):
    stock = serializers.SerializerMethodField()
    measurement_unit = MeasurementUnitSerializer(read_only=True)
    measurement_unit_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "measurement_unit",
            "stock",
            "measurement_unit_id",
        ]

    def get_stock(self, product):
        return product.transaction_set.get_stock_for_product(product=product)


class ProductDetailSerializer(ProductSerializer):
    stand_stocks = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ProductSerializer.Meta.fields + ["stand_stocks"]

    def get_stand_stocks(self, product):
        return product.transaction_set.get_stock_for_product_grouped_by_stand(product)
