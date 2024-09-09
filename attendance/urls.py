from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('todo', views.task_list_view, name='task_list'),
    path('toggle/<int:task_id>/', views.toggle_task_view, name='toggle_task'),
    path('delete/<int:task_id>/', views.delete_task_view, name='delete_task'),
]
