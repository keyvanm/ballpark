from django.contrib import admin

from .models import GenericCurrentAsset, GenericNonCurrentAsset, GenericCurrentLiability, GenericNonCurrentLiability, \
    CashReserve, AccountsReceivable, AccountsPayable

admin.site.register(GenericCurrentAsset)
admin.site.register(GenericNonCurrentAsset)
admin.site.register(GenericCurrentLiability)
admin.site.register(GenericNonCurrentLiability)
admin.site.register(CashReserve)
admin.site.register(AccountsReceivable)
admin.site.register(AccountsPayable)
