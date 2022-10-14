from enum import unique
from django.db import models

# Create your models here.


class Fund(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return str(self.name)

class FundValue(models.Model):
    value = models.DecimalField(max_digits=19, decimal_places=3)
    saved_at = models.DateTimeField(auto_now_add=True)
    fund = models.ForeignKey('Fund', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.value)
