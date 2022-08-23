import factory
import faker

fake = faker.Faker("pt_BR")


class BaseFactory(factory.django.DjangoModelFactory):
    created_at = factory.Faker("date_time_between", start_date="-1y", end_date="now")
    updated_at = factory.Faker("date_time_between", start_date="-1y", end_date="now")
    created_by = factory.SubFactory(
        "apps.users.factories.UserFactory", username="system"
    )
