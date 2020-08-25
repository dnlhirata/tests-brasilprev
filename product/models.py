from django.db import models
from django_extensions.db.models import TimeStampedModel


class Product(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=2000)
    price = models.FloatField()
