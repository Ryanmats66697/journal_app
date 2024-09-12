from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Transaction, Budget, SavingsGoal
from django.shortcuts import render
import json
from django.db.models import Sum

@csrf_exempt
def finance_tracker(request):
    # Query all transactions
    transactions = Transaction.objects.all()

    # Calculate total income (Credits) and total expenses (Debits)
    total_income = transactions.filter(transaction_type='Credit').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expenses = transactions.filter(transaction_type='Debit').aggregate(Sum('amount'))['amount__sum'] or 0

    # Query budgets and savings goals
    budgets = Budget.objects.all()
    savings_goal = SavingsGoal.objects.first()  # Assuming only one savings goal

    # Calculate money left
    money_left = total_income - total_expenses

    # Pass data to the template
    context = {
        'total_income': total_income,
        'total_expenses': total_expenses,
        'money_left': money_left,
        'savings_goal': savings_goal.goal_amount if savings_goal else 0,
        'budgets': budgets,
    }

    return render(request, 'finance.html', context)

@csrf_exempt
def add_transaction(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        transaction_type = request.POST.get('type')

        if description and amount and transaction_type:
            Transaction.objects.create(
                description=description,
                amount=amount,
                transaction_type=transaction_type
            )
            return JsonResponse({'success': True})
    return JsonResponse({'success': False})

@csrf_exempt
def add_budget(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        amount = request.POST.get('amount')

        if category and amount:
            try:
                amount = float(amount)  # Convert amount to float
                Budget.objects.create(
                    category=category,
                    planned_amount=amount
                )
                return JsonResponse({'success': True})
            except Exception as e:
                return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request'})

@csrf_exempt
def save_savings_goal(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            goal = data.get('goal')

            if goal:
                goal = float(goal)
                SavingsGoal.objects.create(goal_amount=goal)
                return JsonResponse({'success': True})
            return JsonResponse({'success': False, 'error': 'Goal is required'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

def get_budget_data(request):
    # Query all expenses from the Transaction model
    expenses = Transaction.objects.filter(transaction_type='Debit')
    categories = expenses.values('description').annotate(total_amount=Sum('amount'))

    data = {
        'labels': [category['description'] for category in categories],
        'values': [float(category['total_amount']) for category in categories],
    }
    return JsonResponse(data)
