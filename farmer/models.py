from django.db import models

# Create your models here.
class Farmer(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    registration_number = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    loan = models.DecimalField(max_digits=10, decimal_places=2)
    savings = models.DecimalField(max_digits=10, decimal_places=2)
    credit_score = models.IntegerField()