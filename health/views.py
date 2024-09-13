from django.shortcuts import render, redirect
from .models import Exercise, Sleep, Meal, HealthGoal
from django.db.models import Sum
from datetime import datetime, timedelta

def health_tracker(request):
    if request.method == 'POST':
        # Handle Exercise Log form submission
        if 'exerciseType' in request.POST:
            exercise_type = request.POST.get('exerciseType')
            duration = request.POST.get('exerciseDuration')
            calories_burned = request.POST.get('caloriesBurned')
            Exercise.objects.create(type=exercise_type, duration=duration, calories_burned=calories_burned)

        # Handle Sleep Log form submission
        elif 'sleepDuration' in request.POST:
            sleep_duration = request.POST.get('sleepDuration')
            sleep_quality = request.POST.get('sleepQuality')
            Sleep.objects.create(duration=sleep_duration, quality=sleep_quality)

        # Handle Meal Log form submission
        elif 'mealDescription' in request.POST:
            meal_description = request.POST.get('mealDescription')
            meal_calories = request.POST.get('mealCalories')
            meal_protein = request.POST.get('mealProtein')
            meal_carbs = request.POST.get('mealCarbs')
            Meal.objects.create(description=meal_description, calories=meal_calories, protein=meal_protein, carbs=meal_carbs)

        # Handle Health Goal form submission
        elif 'goalType' in request.POST:
            goal_type = request.POST.get('goalType')
            goal_target = request.POST.get('goalTarget')
            HealthGoal.objects.create(goal_type=goal_type, target_value=goal_target)


        # Redirect after handling forms to avoid re-submission
        return redirect('health')

    # Fetch existing data for the health tracker
    exercises = Exercise.objects.all()
    sleep_records = Sleep.objects.all()
    meals = Meal.objects.all()
    goals = HealthGoal.objects.all()

    # Aggregate daily data
    today = datetime.today().date()
    days = [today - timedelta(days=i) for i in range(5)]  # Last 5 days

    exercise_data = Exercise.objects.filter(date__in=days)
    meal_data = Meal.objects.filter(date__in=days)

    daily_burnt_calories = []

    for day in days:
        daily_meal_calories = meal_data.filter(date=day).aggregate(Sum('calories'))['calories__sum'] or 0
        daily_exercise_calories = exercise_data.filter(date=day).aggregate(Sum('calories_burned'))['calories_burned__sum'] or 0
        daily_burnt_calories.append(daily_meal_calories - daily_exercise_calories)

    context = {
        'exercises': exercises,
        'sleep_records': sleep_records,
        'meals': meals,
        'goals': goals,
        'daily_burnt_calories': daily_burnt_calories,
        'days': [day.strftime('%Y-%m-%d') for day in days],  # Format days as strings for Chart.js
    }

    return render(request, 'health.html', context)
