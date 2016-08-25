from django.db import models
from djmoney.models.fields import MoneyField

from ballpark.ventures.models import Venture


class AbstractBalanceItem(models.Model):
    venture = models.ForeignKey(Venture)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    amount = MoneyField(max_digits=20, decimal_places=2, default_currency='USD')

    class Meta:
        abstract = True


class AbstractAsset(AbstractBalanceItem):
    class Meta:
        abstract = True


class AbstractCurrentAsset(AbstractAsset):
    class Meta:
        abstract = True


class AbstractNonCurrentAsset(AbstractAsset):
    class Meta:
        abstract = True


class AbstractLiability(AbstractBalanceItem):
    class Meta:
        abstract = True


class AbstractCurrentLiability(AbstractLiability):
    class Meta:
        abstract = True


class AbstractNonCurrentLiability(AbstractLiability):
    class Meta:
        abstract = True


class AbstractEquity(AbstractLiability):
    class Meta:
        abstract = True
