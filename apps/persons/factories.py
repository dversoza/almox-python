import faker
import factory

from apps.core.factories import BaseFactory

fake = faker.Faker("pt_BR")


class PersonFactory(BaseFactory):
    class Meta:
        model = "persons.Person"
        django_get_or_create = ("name",)

    name = factory.Faker("name", locale="pt_BR")
    is_business = False
    document = factory.LazyAttribute(lambda _: fake.cpf())
    phone = factory.LazyAttribute(lambda _: fake.phone_number())
    user = None
    stand = None


class BusinessFactory(PersonFactory):
    name = factory.Faker("company", locale="pt_BR")
    is_business = True
    document = factory.LazyAttribute(lambda _: fake.cnpj())
