from django.contrib.auth.models import (
    BaseUserManager
)
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, phone=None, username=None, first_name=None, last_name=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )

        password=make_password(password)
        user.set_password(password)
        user.phone = phone
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password, phone=None, **extra_fields):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            phone=phone,
            **extra_fields
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, phone, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        user = self.create_user(
            email,
            password=password,
            phone=phone,
            **extra_fields
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user
