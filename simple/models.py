from django.db import models

class Offer(models.Model):
    id = models.IntegerField(
        verbose_name='Offer id',
        name='id',
        auto_created=True,
        primary_key=True,
        unique=True,
        serialize=True,
        null=False
    )
    datetime = models.DateTimeField(
        verbose_name='Date time',
        name='datetime',
        auto_now_add=True,
        null=False
    )
    stock = models.CharField(
        verbose_name='Stock codename',
        name='stock',
        null=False,
        max_length=8
    )
    operation = models.CharField(
        verbose_name='Offer operation',
        name='operation',
        null=False,
        max_length=6
    )
    value = models.DecimalField(
        verbose_name='Offer value',
        name='value',
        decimal_places=2,
        max_digits=32,
        null=False
    )
    shares = models.IntegerField(
        verbose_name='Number of shares',
        name='shares'
    )
    broker = models.CharField(
        verbose_name='Broker id',
        name='broker',
        null=False,
        max_length=64
    )
