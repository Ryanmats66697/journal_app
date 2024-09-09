from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255)
    total_lectures = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Attendance(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lecture_number = models.PositiveIntegerField()
    attended = models.BooleanField(default=False)

    class Meta:
        unique_together = ('course', 'lecture_number')

    def __str__(self):
        return f"{self.course.name} - Lecture {self.lecture_number}"
