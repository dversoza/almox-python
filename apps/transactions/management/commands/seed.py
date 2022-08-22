from django.core.management.base import BaseCommand

from apps.transactions.models import TransactionType

MODE_REFRESH = "refresh"  # Clear all data and creates
MODE_CLEAR = "clear"  # Clear all data and do not create any object


class Command(BaseCommand):
    help = "Seeds database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument("--mode", type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write("Seeding transaction types...")
        run_seed(self, options["mode"])
        self.stdout.write("Done.")


def clear_data():
    """Deletes all transaction types"""
    TransactionType.objects.all().delete()


def create_transaction_types():
    """Creates transaction types"""
    TRANSACTION_TYPES = [
        ("Entrega", "Entrega de produtos do almoxarifado para uma barraca"),
        ("Devolução", "Devolução de produtos de uma barraca para o almoxarifado"),
        ("Compra", "Compra de produtos para o almoxarifado"),
        ("Doação", "Doação de produtos para o almoxarifado"),
    ]
    TransactionType.objects.bulk_create(
        [
            TransactionType(
                name=name,
                description=description,
            )
            for name, description in TRANSACTION_TYPES
        ]
    )


def run_seed(self, mode):
    """Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    # Create transaction types
    create_transaction_types()
