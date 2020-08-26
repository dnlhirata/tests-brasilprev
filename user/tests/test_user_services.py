import pytest
from user import services


@pytest.mark.django_db
def test_user_get_token(user_factory):
    user = user_factory.create()
    expected_token = user.auth_token.key

    token = services.user_get_token(user=user)
    assert expected_token == token


@pytest.mark.django_db
def test_user_create_with_valid_data():
    user_data = {'name': 'John Doe', 'email': 'johndoe@example.com', 'password': 'valid_password', 'cpf': 99999999999}
    user = services.user_create(**user_data)

    assert user.name == user_data.get('name')


@pytest.mark.django_db
def test_user_create_with_invalid_data():
    user_data = {'name': 'John Doe', 'email': 'johndoe@example.com', 'password': 'valid_password'}

    with pytest.raises(TypeError) as excinfo:
        services.user_create(**user_data)


@pytest.mark.django_db
def test_user_login(user_factory):
    user = user_factory.create()
    logged_user = services.user_login(email=user.email, password=user.password)

    assert user == logged_user
