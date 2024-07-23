from django.db import models

class Farmer(models.Model):
    STATUS_CHOICES = [
        ('inactive', 'Inactive'),
        ('active', 'Active'),
    ]

    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    registration_number = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='inactive')
    loan = models.DecimalField(max_digits=10, decimal_places=2)
    savings = models.DecimalField(max_digits=10, decimal_places=2)
    credit_score = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"