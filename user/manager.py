from django.contrib.auth.base_user import BaseUserManager
from rest_framework.exceptions import ValidationError


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        user = self.model(email=email, **extra_fields)
        if not password:
            raise ValidationError("Password cannot be blank")

        user.set_password(password)

        user.is_active = True
        user.is_staff = False
        user.is_superuser = True
        user.username = email

        user.set_password(password)
        user.save(using=self._db)

        return user
