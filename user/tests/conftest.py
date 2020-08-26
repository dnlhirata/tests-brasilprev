from pytest_factoryboy import register

from user.tests.factories import TokenFactory, UserFactory

register(TokenFactory)
register(UserFactory)