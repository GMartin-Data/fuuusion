from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class CryptoApi(models.Model):
    slug = models.CharField(max_length=100, null=False, blank=False)
    convert = models.CharField(max_length=100, null=False, blank=False)

class FlowerFeatures(models.Model):
    sepal_length = models.FloatField(default=6.1, null=False, blank=False)
    sepal_width = models.FloatField(default=2.8, null=False, blank=False)
    petal_length = models.FloatField(default=4.7, null=False, blank=False)
    petal_width = models.FloatField(default=1.2, null=False, blank=False)
