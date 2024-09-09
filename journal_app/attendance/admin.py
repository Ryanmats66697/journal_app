from django.contrib import admin
from .models import Course
from .models import Attendance
# Register your models here.

admin.site.register(Course)
admin.site.register(Attendance)
