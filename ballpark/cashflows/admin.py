from django.contrib import admin


from .models import *
# Register your models here.
admin.site.register(GenericOnetimeIncome)
admin.site.register(GenericRecurringIncome)
admin.site.register(GenericOnetimeExpense)
admin.site.register(GenericRecurringExpense)
