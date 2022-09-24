import codecs
import csv

from apps.products.models import Product
from apps.stands.models import Stand
from django.db import connection
from django.http import HttpResponse
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
    TokenAuthentication,
)
from rest_framework.views import APIView


class ExportCSVProducts(APIView):
    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="Produtos.csv"'
        response.write(codecs.BOM_UTF8)

        writer = csv.writer(
            response, delimiter=";", quotechar='"', quoting=csv.QUOTE_ALL
        )

        headers = ["ID", "Produto", "Unidade de Medida"]

        writer.writerow(headers)

        products = Product.objects.filter(active=True).order_by("name")

        for product in products:
            writer.writerow([product.id, product.name, product.measurement_unit.name])

        return response


class ExportCSVStands(APIView):
    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="Barracas.csv"'
        response.write(codecs.BOM_UTF8)

        writer = csv.writer(
            response, delimiter=";", quotechar='"', quoting=csv.QUOTE_ALL
        )

        headers = ["ID", "Barraca", "Responsável", "Contato"]

        writer.writerow(headers)

        stands = Stand.objects.filter(active=True).order_by("name")

        for stand in stands:
            writer.writerow(
                [
                    stand.id,
                    stand.name,
                    stand.manager.name if stand.manager else "",
                    stand.contact,
                ]
            )

        return response


class ExportStockCSV(APIView):
    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="Estoque.csv"'
        response.write(codecs.BOM_UTF8)

        writer = csv.writer(
            response, delimiter=";", quotechar='"', quoting=csv.QUOTE_ALL
        )

        headers = [
            "Barraca",
            "Produto",
            "Entradas",
            "Saídas",
            "Saldo",
        ]

        writer.writerow(headers)

        with connection.cursor() as cursor:
            stock = cursor.execute(
                """
                SELECT
                    s.name Barraca,
                    p.name Produto,
                    (SELECT SUM(CAST(quantity AS DECIMAL)) FROM transactions_transaction t WHERE t.to_stand_id = s.id AND p.id = t.product_id) || ' ' || lower(pm.abbreviation) || 's' AS Entradas,
                    (SELECT SUM(CAST(quantity AS DECIMAL)) FROM transactions_transaction t WHERE t.from_stand_id = s.id AND p.id = t.product_id) || ' ' || lower(pm.abbreviation) || 's' AS Saídas,
                    COALESCE(
                        (SELECT SUM(CAST(quantity AS DECIMAL)) FROM transactions_transaction t WHERE t.to_stand_id = s.id AND p.id = t.product_id) -
                        (SELECT SUM(CAST(quantity AS DECIMAL)) FROM transactions_transaction t WHERE t.from_stand_id = s.id AND p.id = t.product_id),
                    (SELECT SUM(CAST(quantity AS DECIMAL)) FROM transactions_transaction t WHERE t.to_stand_id = s.id AND p.id = t.product_id)
                    ) || ' ' || lower(pm.abbreviation) || 's' AS Estoque
                FROM stands_stand s, products_product p
                LEFT JOIN products_measurementunit pm ON pm.id = p.measurement_unit_id
                WHERE (SELECT SUM(quantity) FROM transactions_transaction t WHERE t.to_stand_id = s.id AND p.id = t.product_id) IS NOT NULL
                GROUP BY s.id, p.id, pm.id
                """
            )

            for row in stock:
                writer.writerow(row)

        return response
