from django.db import models
from django_extensions.db.models import TimeStampedModel
from djmoney.models.fields import MoneyField
from model_utils import Choices

from ballpark.ventures.models import Venture


class AbstractCashFlow(TimeStampedModel):
    venture = models.ForeignKey(Venture)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    amount = MoneyField(max_digits=20, decimal_places=2, default_currency='USD')

    class Meta:
        abstract = True


class AbstractIncome(AbstractCashFlow):
    class Meta:
        abstract = True


class AbstractExpense(AbstractCashFlow):
    class Meta:
        abstract = True


class Occurable(models.Model):
    date = models.DateField()
    frequency = None

    class Meta:
        abstract = True


class OnetimeOccurable(Occurable):
    frequency = 'onetime'

    class Meta:
        abstract = True


class RecurringOccurable(Occurable):
    FREQUENCY_CHOICES = Choices('hourly', 'daily', 'weekdays', 'weekends', 'weekly', 'biweekly', 'monthly', 'yearly')
    frequency = models.CharField(choices=FREQUENCY_CHOICES, max_length=15)

    class Meta:
        abstract = True
