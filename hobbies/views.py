from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Hobby, Goal

def hobbies_tracker(request):
    return render(request, 'hobbies.html')

def get_hobbies(request):
    hobbies = Hobby.objects.filter(user=request.user).values('id', 'name', 'time_spent')
    return JsonResponse({'hobbies': list(hobbies)})

def get_goals(request):
    goals = Goal.objects.filter(user=request.user).select_related('hobby').values('hobby__name', 'target_hours')
    return JsonResponse({'goals': list(goals)})

@csrf_exempt
def add_hobby(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        hobby_name = data.get('name')
        time_spent = data.get('time_spent')
        if hobby_name and time_spent:
            Hobby.objects.create(user=request.user, name=hobby_name, time_spent=time_spent)
            return JsonResponse({'success': True})
    return JsonResponse({'success': False})

@csrf_exempt
def set_goal(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        hobby_id = data.get('hobby_id')
        target_hours = data.get('target_hours')
        if hobby_id and target_hours:
            hobby = Hobby.objects.get(id=hobby_id)
            Goal.objects.create(user=request.user, hobby=hobby, target_hours=target_hours)
            return JsonResponse({'success': True})
    return JsonResponse({'success': False})
