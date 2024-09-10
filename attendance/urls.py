from django.urls import path
from .views import attendance_tracker, add_course, mark_attendance, get_attendance_data

urlpatterns = [
    path('attendance/', attendance_tracker, name='attendance_tracker'),
    path('add-course/', add_course, name='add_course'),
    path('mark-attendance/', mark_attendance, name='mark_attendance'),
    path('get-attendance-data/', get_attendance_data, name='get_attendance_data'),
    #path('get-courses/', get_courses, name='get_courses'),
]
