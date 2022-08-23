import faker
import factory

from apps.core.factories import BaseFactory

fake = faker.Faker("pt_BR")


class ProductFactory(BaseFactory):
    class Meta:
        model = "products.Product"
        django_get_or_create = ("name",)

    name = factory.Faker("name", locale="pt_BR")
    description = factory.Faker("text", max_nb_chars=100, locale="pt_BR")
    measurement_unit = factory.SubFactory(
        "apps.products.factories.MeasurementUnitFactory", name="Unidade"
    )


class MeasurementUnitFactory(BaseFactory):
    class Meta:
        model = "products.MeasurementUnit"
        django_get_or_create = ("name",)

    name = fake.name()
    abbreviation = factory.LazyAttribute(lambda obj: obj.name[0:2])
