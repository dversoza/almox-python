import random
from datetime import timezone

import factory
import faker

from apps.core.factories import BaseFactory
from apps.persons.models import Person
from apps.products.models import Product
from apps.stands.models import Stand
from apps.transactions.models import OPERATIONS, TransactionType

fake = faker.Faker("pt_BR")


class TransactionFactory(BaseFactory):
    class Meta:
        model = "transactions.Transaction"

    datetime = factory.Faker(
        "date_time_between", start_date="-1y", end_date="now", tzinfo=timezone.utc
    )
    stand = factory.Iterator(Stand.objects.all())
    product = factory.Iterator(Product.objects.all())
    person = factory.Iterator(Person.objects.all())
    operation = factory.LazyAttribute(lambda _: random.choice(OPERATIONS)[0])
    type = factory.Iterator(TransactionType.objects.all())
    quantity = factory.LazyAttribute(
        lambda _: fake.pyfloat(left_digits=2, right_digits=2, positive=True)
    )
    price = factory.LazyAttribute(lambda _: fake.pyint(min_value=100, max_value=10000))
    details = factory.LazyAttribute(lambda _: fake.text(max_nb_chars=100))


class TransactionTypeFactory(BaseFactory):
    class Meta:
        model = "transactions.TransactionType"
        django_get_or_create = ("name",)

    operation = random.choice(OPERATIONS)[0]
    name = factory.LazyAttribute(lambda obj: obj.operation.capitalize())
    description = factory.LazyAttribute(lambda obj: obj.name.capitalize())
