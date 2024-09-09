from django.db import models
from django.utils import timezone

class Transaction(models.Model):
    DESCRIPTION_CHOICES = [
        ('Credit', 'Credit'),
        ('Debit', 'Debit'),
    ]
    description = models.CharField(max_length=255, default="Unknown")  # Provide a default value
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(choices=DESCRIPTION_CHOICES, max_length=10)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.description} - {self.transaction_type} - {self.amount}"

class Budget(models.Model):
    category = models.CharField(max_length=255)
    planned_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.category} - {self.planned_amount}"

class SavingsGoal(models.Model):
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Savings Goal - {self.goal_amount}"

