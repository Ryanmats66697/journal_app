from django.urls import path
from .views import hobbies, add_hobby, set_goal, get_hobbies, get_goals

urlpatterns = [
    path('hobbies/', hobbies, name='hobbies_tracker'),
    path('add_hobby/', add_hobby, name='add_hobby'),
    path('set_goal/', set_goal, name='set_goal'),
    path('get_hobbies/', get_hobbies, name='get_hobbies'),
    path('get_goals/', get_goals, name='get_goals'),
]
