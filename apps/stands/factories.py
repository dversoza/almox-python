import factory
import faker

from apps.core.factories import BaseFactory

fake = faker.Faker("pt_BR")


class StandFactory(BaseFactory):
    class Meta:
        model = "stands.Stand"
        django_get_or_create = ("name",)

    name = factory.Faker("company", locale="pt_BR")
    active = True
    contact = factory.Faker("phone_number", locale="pt_BR")
    manager = factory.SubFactory("apps.persons.factories.PersonFactory", name="Admin")
