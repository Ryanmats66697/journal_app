from django.shortcuts import render, redirect
from .models import Task


#view for todo_page

def task_list_view(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        # Handle adding new task
        new_task_text = request.POST.get('new_task')
        if new_task_text:
            Task.objects.create(text=new_task_text)
        return redirect('task_list')

    return render(request, 'hobbies.html', {'tasks': tasks})


def toggle_task_view(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')


def delete_task_view(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')

