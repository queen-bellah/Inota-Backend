from django.db import models
from farmer.models import Farmer

class Loan(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    amount_repaid = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='loans')

    def __str__(self):
          return f"{self.farmer}"