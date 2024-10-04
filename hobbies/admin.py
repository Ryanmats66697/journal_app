from django.contrib import admin
from .models import Hobby, HobbyGoal  # Import the correct models

# Register the models with the admin site
admin.site.register(Hobby)
admin.site.register(HobbyGoal)
