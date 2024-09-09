from django.urls import path
from . import views

urlpatterns = [
    path('add-transaction/', views.add_transaction, name='add_transaction'),
    path('add-budget/', views.add_budget, name='add_budget'),
    path('save-goal/', views.save_savings_goal, name='save_savings_goal'),
    path('finance/', views.finance_tracker, name='finance_tracker'),
    path('get-budget-data/', views.get_budget_data, name='get_budget_data'),
]
