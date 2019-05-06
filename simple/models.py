from django.db import models

class Offer(models.Model):
    epoch = models.DecimalField(
        verbose_name='Epoch time',
        name='epoch',
        primary_key=True,
        decimal_places=4,
        max_digits=16,
        null=False
    )
    date_time = models.DateTimeField(
        verbose_name='Date and time of publishing',
        name='date time',
        null=False
    )
    stock = models.CharField(
        verbose_name='Stock codename',
        name='stock id',
        null=False,
        max_length=8
    )
    operation = models.CharField(
        verbose_name='Offer operation',
        name='offer operation',
        null=False,
        max_length=6
    )
    value = models.DecimalField(
        verbose_name='Offer value',
        name='value',
        decimal_places=4,
        max_digits=32,
        null=False
    )
    quantity = models.IntegerField(
        verbose_name='Number of shares',
        name='shares'
    )
    broker = models.CharField(
        verbose_name='Broker identification code',
        name='broker id',
        null=False,
        max_length=64
    )
