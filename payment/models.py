from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Payment(models.Model):
    amount = models.FloatField()
    payer_name = models.CharField(max_length=100)
    payer_email = models.EmailField(null=True)
    payer_phone = models.PositiveIntegerField(null=True)
    transaction_id = models.CharField(max_length=100)
    payment_status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of ${self.amount} by {self.payer_name}"
