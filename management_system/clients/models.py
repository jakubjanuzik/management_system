from django.db import models
from django_countries.fields import CountryField
from decimal import Decimal


class Client(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()


class ClientAddressInfo(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=256)
    address_line_2 = models.CharField(max_length=256)
    city = models.CharField(max_length=64)
    country = CountryField()


class Invoice(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    number = models.IntegerField()
    date = models.DateField()
    paid_date = models.DateField()


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(
        Invoice, related_name="items", unique=False, on_delete=models.CASCADE
    )
    description = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.DecimalField(max_digits=8, decimal_places=2, default=1)

    def total(self):
        total = Decimal(str(self.unit_price * self.quantity))
        return total.quantize(Decimal("0.01"))
