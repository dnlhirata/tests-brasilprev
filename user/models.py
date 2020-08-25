from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, User
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _

from user.manager import UserManager


class StoreUser(User, TimeStampedModel):
    name = models.CharField(max_length=100, null=False, verbose_name=_("Name"))
    cpf = models.CharField(max_length=11, null=False, verbose_name=_("CPF"), unique=True)
    gender = models.CharField(max_length=50, default="Undefined", null=True, blank=True, verbose_name=_("Gender"))
    birth_date = models.DateField(null=True, blank=True, verbose_name=_("Birth date"))

    USERNAME_FIELD = "email"

    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
