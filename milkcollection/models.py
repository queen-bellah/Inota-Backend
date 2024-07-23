from django.db import models
from farmer.models import Farmer


# Create your models here.
class MilkCollection(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='milk_collections')
    date = models.DateField()
    liters = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.TimeField()
    amount_of_money = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
          return f"{self.farmer}"