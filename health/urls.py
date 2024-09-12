from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health_tracker, name='health'),
]
