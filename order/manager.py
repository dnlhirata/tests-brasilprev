from django.db import models

from product.models import Product


class OrderProductManager(models.Manager):
    def bulk_create(self, objs, batch_size=None, ignore_conflicts=False):
        for obj in objs:
            product = Product.objects.get(id=obj.product_id)
            product.quantity -= obj.quantity
            product.save()

            obj.save()
