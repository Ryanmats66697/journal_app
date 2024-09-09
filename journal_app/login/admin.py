from django.contrib import admin
from .models import UserProfile  # Replace with your model

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'date_of_birth', 'bio')  # Fields to display in the list view
    search_fields = ('user__username', 'first_name', 'last_name')  # Fields to search in the admin interface

admin.site.register(UserProfile, UserProfileAdmin)  # Register the model and admin class
