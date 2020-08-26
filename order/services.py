from typing import Union

from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

from order.models import Order, OrderProduct
from product.models import Product


def order_create(user: User, items: list) -> Order:
    order = Order.objects.create(user=user)
    try:
        order_products = []
        for item in items:
            product = Product.objects.get(id=item.get('product'))

            if product.quantity < item.get('quantity'):
                raise ValidationError(
                    'There are not enough {product} in stock. Only have {quantity}'.format(product=product.name,
                                                                                           quantity=product.quantity))

            order_products.append(OrderProduct(order=order, product=product, quantity=item.get('quantity')))
    except Product.DoesNotExist:
        order.delete()
        raise ValidationError('One or more product does not exist')

    OrderProduct.objects.bulk_create(order_products)
    return order


def order_get_orders_from_user(user: User) -> list:
    orders = user.orders.all()

    orders_details = []
    for order in orders:
        order_detail = {'order': order.id, 'products': OrderProduct.objects.filter(order_id=order.id),
                        'date': order.created}
        orders_details.append(order_detail)

    return orders_details
