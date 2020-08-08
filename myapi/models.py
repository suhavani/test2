from django.db import models
from djmoney.models.fields import MoneyField
class food(models.Model):
    name = models.CharField(max_length=60)
    price= MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    description = models.TextField(blank = True)
    calories = models.IntegerField()
    isbest= models.CharField(max_length=60)
     
    def __str__(self):
        return self.name
