from django.urls import path
from . import views

urlpatterns = [
    path('hobbies/', views.hobbies_tracker, name='hobbies_tracker'),
    path('get_hobbies/', views.get_hobbies, name='get_hobbies'),
    path('get_goals/', views.get_goals, name='get_goals'),
    path('add_hobby/', views.add_hobby, name='add_hobby'),  # Add this
    path('set_goal/', views.set_goal, name='set_goal'),      # Add this
]
