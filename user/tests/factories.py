import factory
from faker import Factory
from rest_framework.authtoken.models import Token
from user.models import User, StoreUser
from user.tests.providers import DocumentProvider

faker = Factory.create()
faker.add_provider(DocumentProvider)


class TokenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Token


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StoreUser

    name = factory.Faker("name")
    email = factory.Faker("email")
    password = factory.Faker("password")
    auth_token = factory.RelatedFactory(TokenFactory, "user")
    cpf = faker.cpf()
