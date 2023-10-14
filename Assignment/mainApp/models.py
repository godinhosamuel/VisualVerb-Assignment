from django.db import models
from datetime import date,datetime

# Model to store Super Market Sales data
class SupermarketSale(models.Model):
    invoice_id = models.CharField(primary_key=True, max_length=50)
    product_line = models.CharField(max_length=50)
    unit_price = models.FloatField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    tax = models.FloatField(default=0)
    total = models.FloatField(default=0)
    date = models.DateField(default=date.today)
    time = models.TimeField(default=None, null=True, blank=True)