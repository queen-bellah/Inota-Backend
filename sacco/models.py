from django.db import models

# Create your models here.
class Sacco(models.Model):
    name = models.CharField(max_length=40)
    registration_number = models.CharField(max_length=50)
    total_farmers = models.IntegerField()
    total_loans_given = models.DecimalField(max_digits=10, decimal_places=2)
    total_loans_repaid = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
          return f"{self.name}-{self.registration_number}"