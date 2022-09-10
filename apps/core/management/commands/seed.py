from apps.persons.factories import BusinessFactory, PersonFactory
from apps.persons.models import Person
from apps.products.factories import MeasurementUnitFactory, ProductFactory
from apps.products.models import MeasurementUnit, Product
from apps.stands.factories import StandFactory
from apps.stands.models import Stand
from apps.transactions.factories import TransactionFactory, TransactionTypeFactory
from apps.transactions.models import Transaction, TransactionType
from django.contrib.auth.models import Group, User
from django.core.management.base import BaseCommand
from datetime import datetime

from apps.users.factories import UserFactory

MODE_REFRESH = "refresh"  # Clear all data and creates
MODE_CLEAR = "clear"  # Clear all data and do not create any object


class Command(BaseCommand):
    help = "Seeds database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument("--mode", type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write("Seeding database...")
        self._run_seed(options["mode"])
        self.stdout.write("Done.")

    def _clear_data(self):
        """Deletes all transaction types"""
        Transaction.objects.all().delete()
        TransactionType.objects.all().delete()
        Product.objects.all().delete()
        MeasurementUnit.objects.all().delete()
        Stand.objects.all().delete()

    def _run_seed(self, mode):
        """Seed database based on mode

        :param mode: refresh / clear
        :return:
        """
        if mode == MODE_CLEAR:
            # Clear data from tables
            self._clear_data()
            return

        # Clear data from tables and create new data
        self.__seed_groups()
        self.__seed_users()
        self.__seed_persons()
        self.__seed_products()
        self.__seed_stands()
        self.__seed_transactions()

    def __seed_groups(self):
        # Creates groups
        self.stdout.write("Seeding Groups ...")

        self.admin_group, _ = Group.objects.get_or_create(name="Administradores")
        self.staff_group, _ = Group.objects.get_or_create(name="Coordenação")
        self.default_group, _ = Group.objects.get_or_create(name="Padrão")

    def __seed_users(self):
        # Creates users
        self.stdout.write("Seeding Users ...")

        self.admin = UserFactory(
            username="admin",
            email="admin@example.com",
            is_staff=True,
            is_superuser=True,
        )
        self.system = UserFactory(
            username="system",
            email="system@example.com",
            is_staff=True,
        )
        self.default_user = UserFactory(
            username="default",
            email="default@example.com",
            is_staff=False,
        )

        self.admin.groups.add(self.admin_group)
        self.admin.set_password("password")
        self.admin.save()

        self.system.groups.add(self.staff_group)
        self.system.set_password("password")
        self.system.save()

        self.default_user.groups.add(self.default_group)
        self.default_user.set_password("password")
        self.default_user.save()

    def __seed_persons(self):
        # Creates persons
        self.stdout.write("Seeding Persons ...")

        PersonFactory(name="Admin", user=self.admin)

        PersonFactory.create_batch(5)
        BusinessFactory.create_batch(5)

    def __seed_products(self):
        # Creates products and measurement units
        self.stdout.write("Seeding Measurement Units ...")

        un = MeasurementUnitFactory(name="Unidade", abbreviation="un")
        kg = MeasurementUnitFactory(name="Quilograma", abbreviation="kg")
        cx = MeasurementUnitFactory(name="Caixa", abbreviation="cx")
        l = MeasurementUnitFactory(name="Litro", abbreviation="l")
        pcte = MeasurementUnitFactory(name="Pacote", abbreviation="pcte")
        lt = MeasurementUnitFactory(name="Lata", abbreviation="lt")

        self.stdout.write("Seeding Products ...")
        ProductFactory(
            name="Pão de queijo",
            description="Pão de queijo quentinho",
            measurement_unit=un,
        )
        ProductFactory(
            name="Misto quente", description="Misto quente frio", measurement_unit=un
        )
        ProductFactory(name="Pão", description="Pão francês", measurement_unit=kg)
        ProductFactory(
            name="Pão de alho", description="Pão de alho", measurement_unit=kg
        )
        ProductFactory(
            name="Pão de batata", description="Pão de batata", measurement_unit=kg
        )
        ProductFactory(name="Ovos", description="Dúzia de ovos", measurement_unit=cx)
        ProductFactory(
            name="Leite condensado",
            description="Leite condensado caixa",
            measurement_unit=cx,
        )
        ProductFactory(name="Água", description="Água", measurement_unit=l)
        ProductFactory(name="Leite", description="Leite", measurement_unit=l)
        ProductFactory(name="Bolacha", description="Bolacha", measurement_unit=pcte)
        ProductFactory(name="Biscoito", description="Biscoito", measurement_unit=pcte)
        ProductFactory(
            name="Coca-Cola", description="Coca-Cola lata", measurement_unit=lt
        )
        ProductFactory(name="Pepsi", description="Pepsi lata", measurement_unit=lt)

    def __seed_stands(self):
        # Creates stands
        self.stdout.write("Seeding Stands ...")

        StandFactory.create_batch(5)

    def __seed_transactions(self):
        # Creates transaction types
        self.stdout.write("Seeding Transaction Types ...")

        TransactionTypeFactory(
            operation="S",
            name="Entrega",
            description="Entrega de produtos do almoxarifado para uma barraca",
        )
        TransactionTypeFactory(
            operation="S",
            name="Restituição",
            description="Restituição de produtos do almoxarifado para um fornecedor",
        )
        TransactionTypeFactory(
            operation="E",
            name="Devolução",
            description="Devolução de produtos de uma barraca para o almoxarifado",
        )
        TransactionTypeFactory(
            operation="E",
            name="Compra",
            description="Compra de produtos para o almoxarifado",
        )
        TransactionTypeFactory(
            operation="E",
            name="Doação",
            description="Doação de produtos para o almoxarifado",
        )

        self.stdout.write("Seeding Transactions ...")

        for _ in range(15):
            TransactionFactory()
