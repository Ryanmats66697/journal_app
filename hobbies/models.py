from django.db import models

class Hobby(models.Model):
    name = models.CharField(max_length=100)
    time_spent = models.FloatField(default=0)

    def __str__(self):
        return self.name

class HobbyGoal(models.Model):  # Ensure this class is named HobbyGoal
    hobby = models.ForeignKey(Hobby, on_delete=models.CASCADE)
    target_hours = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.hobby.name}: {self.target_hours} hours/week"
