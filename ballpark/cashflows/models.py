from __future__ import unicode_literals

from django_extensions.db.models import TimeStampedModel

from .behaviors import AbstractIncome, AbstractExpense, OnetimeOccurable, RecurringOccurable


class AbstractOnetimeIncome(OnetimeOccurable, AbstractIncome):
    class Meta:
        abstract = True


class AbstractRecurringIncome(RecurringOccurable, AbstractIncome):
    class Meta:
        abstract = True


class AbstractOnetimeExpense(OnetimeOccurable, AbstractExpense):
    class Meta:
        abstract = True


class AbstractRecurringExpense(RecurringOccurable, AbstractExpense):
    class Meta:
        abstract = True


class GenericOnetimeIncome(AbstractOnetimeIncome):
    pass


class GenericRecurringIncome(AbstractRecurringIncome):
    pass


class GenericOnetimeExpense(AbstractOnetimeExpense):
    pass


class GenericRecurringExpense(AbstractRecurringExpense):
    pass
