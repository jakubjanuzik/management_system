from clients.models import Client, ClientAddressInfo, Invoice, InvoiceItem
from django.contrib import admin


class ClientAddressInfoInline(admin.TabularInline):
    model = ClientAddressInfo


class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    readonly_fields = ("total",)


class ClientAdmin(admin.ModelAdmin):
    inlines = [
        ClientAddressInfoInline,
    ]


class InvoiceAdmin(admin.ModelAdmin):
    inlines = [
        InvoiceItemInline,
    ]


admin.site.register(Client, ClientAdmin)
admin.site.register(Invoice, InvoiceAdmin)
