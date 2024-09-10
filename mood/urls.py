from django.urls import path
from . import views

urlpatterns = [
    path('mood-trends/', views.mood_trends, name='mood_trends'),
    path('mood-tracker/', views.mood_tracker, name='mood_tracker'),
]
