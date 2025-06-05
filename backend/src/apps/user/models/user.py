from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


error_msg = "{} is required to login"


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if username is None:
            raise TypeError(error_msg.format("username"))

        user = self.model(username=username, **extra_fields)
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        if username is None:
            raise TypeError(error_msg.format("username"))
        if password is None:
            raise TypeError(error_msg.format("password"))

        user = self.create_user(
            username=username,
            password=password,
        )

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        unique=True, null=True, max_length=100, help_text="username of user"
    )

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True, help_text="is active")

    objects = UserManager()

    created_at = models.DateTimeField(auto_now_add=True, help_text="created at")
    updated_at = models.DateTimeField(auto_now=True, help_text="updated at")

    firstname = models.CharField(
        max_length=30, blank=True, null=True, help_text="first name of user"
    )
    lastname = models.CharField(
        max_length=30, blank=True, null=True, help_text="last name of user"
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
