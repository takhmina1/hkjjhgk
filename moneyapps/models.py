from django.db import models

class Transaction(models.Model):
    wallet = models.CharField(max_length=255)
    amount_sent = models.DecimalField(max_digits=20, decimal_places=8)
    currency_sent = models.CharField(max_length=5)
    amount_received = models.DecimalField(max_digits=20, decimal_places=8)
    currency_received = models.CharField(max_length=5)
    commission = models.DecimalField(max_digits=5, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.id}: {self.amount_sent} {self.currency_sent} -> {self.amount_received} {self.currency_received}"
