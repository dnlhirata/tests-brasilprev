from django.db import IntegrityError
from rest_framework.exceptions import ValidationError

from product.models import Product


def product_create(name: str, price: float, **kwargs) -> Product:
    try:
        product = Product.objects.create(name=name, price=price, **kwargs)
    except IntegrityError:
        raise ValidationError('A product with this name already exists')

    return product


def product_get_list(**kwargs) -> list:
    if kwargs.get('name'):
        return Product.objects.filter(name__contains=kwargs.get('name'))

    return Product.objects.all()


def product_get_detail(id: int) -> Product:
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise ValidationError('This product does not exist')

    return product


def product_update(id: int, **kwargs) -> Product:
    try:
        product = Product.objects.get(id=id)

        for (key, value) in kwargs.items():
            setattr(product, key, value)

        product.save()
    except Product.DoesNotExist:
        raise ValidationError('This product does not exist')

    return product


def product_delete(id: int) -> None:
    try:
        product = Product.objects.get(id=id)
        product.delete()
    except Product.DoesNotExist:
        raise ValidationError('This product does not exist')
