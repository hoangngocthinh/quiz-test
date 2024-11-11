from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from core.models import UuidTimeStamModel


class User(AbstractUser):
    email = models.EmailField(_("email address"), blank=True, unique=True)
    avatar = models.CharField(null=True, blank=True, max_length=1200)
    avatar_thumb = models.CharField(null=True, blank=True, max_length=1200)
    phone = models.CharField(default="", blank=True, max_length=30)
    bio = models.CharField(default="", blank=True, max_length=1000)
    enabled_2fa = models.BooleanField(default=False)
    description = models.CharField(default="", blank=True, max_length=1000)

    class Meta(AbstractUser.Meta):
        ordering = ("username",)


class Country(UuidTimeStamModel):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=255)


class Address(UuidTimeStamModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    unit_number = models.CharField(max_length=50, blank=True)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
