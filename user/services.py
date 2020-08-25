from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from user.models import StoreUser


def user_create(name: str, email: str, password: str, cpf: str, **kwargs) -> StoreUser:
    user = StoreUser.objects.create_user(name=name, email=email, password=password, cpf=cpf, **kwargs)
    return user


def user_get_token(*, user: StoreUser) -> str:
    token, created = Token.objects.get_or_create(user=user)
    return token.key


def user_login(*, email: str, password: str) -> StoreUser:
    user = authenticate(username=email, password=password)
    if not user:
        raise PermissionError("Invalid email or password")
    return user
