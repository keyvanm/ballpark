from __future__ import unicode_literals

from .behaviors import AbstractCurrentAsset, AbstractCurrentLiability, AbstractNonCurrentAsset, AbstractNonCurrentLiability


class GenericCurrentAsset(AbstractCurrentAsset):
    pass


class GenericNonCurrentAsset(AbstractNonCurrentAsset):
    pass


class GenericCurrentLiability(AbstractCurrentLiability):
    pass


class GenericNonCurrentLiability(AbstractNonCurrentLiability):
    pass


class CashReserve(AbstractCurrentAsset):
    pass


class AccountsReceivable(AbstractCurrentAsset):
    pass


class AccountsPayable(AbstractCurrentLiability):
    pass
