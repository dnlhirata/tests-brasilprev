from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel
from django.db import models

from order.manager import OrderProductManager
from product.models import Product


class Order(TimeStampedModel):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='orders')


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orders_products')
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField()

    objects = OrderProductManager()
