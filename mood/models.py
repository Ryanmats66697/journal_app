from django.db import models

class MoodEntry(models.Model):
    MOOD_CHOICES = [
        ('Happy', 'Happy'),
        ('Neutral', 'Neutral'),
        ('Sad', 'Sad'),
        ('Stressed', 'Stressed'),
        ('Angry', 'Angry'),
    ]
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES)
    factors = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.mood} on {self.date}"
