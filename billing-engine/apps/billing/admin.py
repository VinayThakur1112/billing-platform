from django.contrib import admin
from .models import (
    Account,
    Subscription,
    BillingEvent,
    Invoice,
    InvoiceLineItem,
)

admin.site.register(Account)
admin.site.register(Subscription)
admin.site.register(BillingEvent)
admin.site.register(Invoice)
admin.site.register(InvoiceLineItem)