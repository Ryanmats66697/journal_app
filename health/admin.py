from django.contrib import admin
from .models import HealthGoal
from .models import Exercise
from .models import Sleep
from .models import Meal

# Register your models here.

admin.site.register(HealthGoal)
admin.site.register(Exercise)
admin.site.register(Sleep)
admin.site.register(Meal)
