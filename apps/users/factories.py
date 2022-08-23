import factory
import faker
from django.contrib.auth.models import Group, User

fake = faker.Faker("pt_BR")


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("username",)

    username = fake.user_name()
    password = fake.password()
    email = fake.email()
    is_staff = False
    is_superuser = False
    is_active = True
    last_login = fake.date_time_between(start_date="-1y", end_date="now")
    date_joined = fake.date_time_between(start_date="-1y", end_date="now")


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Group
        django_get_or_create = ("name",)

    name = fake.name()
