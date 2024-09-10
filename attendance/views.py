# views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Course, Attendance
from django.views.decorators.csrf import csrf_exempt
import json


def attendance_tracker(request):
    return render(request, 'attendance.html')


@csrf_exempt
def add_course(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            total_lectures = int(data.get('totalLectures', 0))

            if name and total_lectures > 0:
                course, created = Course.objects.get_or_create(name=name, defaults={'total_lectures': total_lectures})
                if not created:
                    # If course already exists, update the total lectures if necessary
                    course.total_lectures = max(course.total_lectures, total_lectures)
                    course.save()

                # Initialize attendance if not already present
                for lecture_number in range(1, total_lectures + 1):
                    Attendance.objects.get_or_create(course=course, lecture_number=lecture_number,
                                                     defaults={'attended': False})

                return JsonResponse({'success': True, 'course_id': course.id})
            return JsonResponse({'success': False, 'error': 'Invalid data'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': f'Error: {str(e)}'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


@csrf_exempt
@csrf_exempt
def mark_attendance(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            course_id = data.get('courseId')
            lecture_number = data.get('lectureNumber')
            attended = data.get('attended')

            if course_id and lecture_number is not None:
                course = Course.objects.get(id=course_id)
                attendance, created = Attendance.objects.update_or_create(
                    course=course,
                    lecture_number=lecture_number,
                    defaults={'attended': attended}
                )
                return JsonResponse({'success': True})
            return JsonResponse({'success': False, 'error': 'Invalid data'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': f'Error: {str(e)}'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})



def get_attendance_data(request):
    courses = Course.objects.all()
    data = {
        'courses': [
            {
                'id': course.id,
                'name': course.name,
                'attendance': [
                    {
                        'lecture': att.lecture_number,
                        'attended': att.attended
                    }
                    for att in Attendance.objects.filter(course=course)
                ]
            }
            for course in courses
        ]
    }
    return JsonResponse(data)



# If get_courses is not needed, remove or comment it out.
# def get_courses(request):
#     ...
