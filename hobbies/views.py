from django.shortcuts import render
from django.http import JsonResponse
from .models import Hobby, HobbyGoal
from django.db.models import Sum
import json

def hobbies(request):
    return render(request, 'hobbies.html')

def add_hobby(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        hobby_name = data.get('name')
        time_spent = data.get('time_spent')

        Hobby.objects.create(name=hobby_name, time_spent=time_spent)
        return JsonResponse({'success': True})

    return JsonResponse({'success': False})

def get_hobbies(request):
    hobbies = Hobby.objects.values('id', 'name').annotate(total_time_spent=Sum('time_spent'))
    return JsonResponse({'hobbies': list(hobbies)})

def set_goal(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        hobby_id = data.get('hobby_id')
        target_hours = data.get('target_hours')

        Goal.objects.create(hobby_id=hobby_id, target_hours=target_hours)
        return JsonResponse({'success': True})

    return JsonResponse({'success': False})

def get_goals(request):
    goals = Goal.objects.all().select_related('hobby')
    return JsonResponse({'goals': list(goals.values('id', 'target_hours', hobby__name='hobby__name'))})
