from django.db import models
from django.utils import timezone

class Exercise(models.Model):
    type = models.CharField(max_length=100)
    duration = models.IntegerField()  # Duration in minutes
    calories_burned = models.IntegerField()
    date = models.DateField(default=timezone.now)  # Track the date

    def __str__(self):
        return self.type

class Sleep(models.Model):
    duration = models.IntegerField()  # Duration in hours
    quality = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.duration} hours, {self.quality} quality"

class Meal(models.Model):
    description = models.CharField(max_length=255)
    calories = models.IntegerField()
    protein = models.IntegerField()
    carbs = models.IntegerField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.description

class HealthGoal(models.Model):
    goal_type = models.CharField(max_length=50)  # Exercise, Sleep, Nutrition
    target_value = models.IntegerField()  # Target value (e.g., 5 workouts per week)

    def __str__(self):
        return f"{self.goal_type}: {self.target_value}"
