from django.contrib import admin
from .models import Transaction
from .models import Budget
from .models import SavingsGoal

admin.site.register(Transaction)
admin.site.register(Budget)
admin.site.register(SavingsGoal)