from django.db import models
from django.contrib.auth.models import User

class Hobby(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    time_spent = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hobby = models.ForeignKey(Hobby, on_delete=models.CASCADE)
    target_hours = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.hobby.name} - {self.target_hours} hours"
