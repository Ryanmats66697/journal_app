from django.shortcuts import render
from django.http import JsonResponse
from .models import MoodEntry  # This is your model for mood tracking
from datetime import datetime

def mood_tracker(request):
    if request.method == 'POST':
        mood = request.POST.get('mood')
        factors = request.POST.get('moodFactors')
        # Save mood entry to the database
        MoodEntry.objects.create(mood=mood, factors=factors, date=datetime.now())
        return JsonResponse({'success': True})

    # For GET requests, render the mood tracking page
    return render(request, 'mood.html')


from django.http import JsonResponse
from .models import MoodEntry  # Ensure you're importing the correct model
from datetime import datetime, timedelta


def mood_trends(request):
    # Get the date range from query parameters
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # Query mood data based on the date range
    if start_date and end_date:
        mood_data = MoodEntry.objects.filter(date__range=[start_date, end_date]).order_by('date')
    else:
        mood_data = MoodEntry.objects.all().order_by('-date')[:7]  # Default to last 7 records if no range provided

    # Format data for the chart
    dates = [mood.date.strftime('%Y-%m-%d') for mood in mood_data]
    moods = [mood.mood for mood in mood_data]  # Adjust according to your model fields

    return JsonResponse({'dates': dates, 'moods': moods})



