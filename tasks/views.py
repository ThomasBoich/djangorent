from django.shortcuts import render

from tasks.models import Task


# Create your views here.

def all_tasks(request):
    tasks = Task.objects.all()
    context = {
        'active': 'active',
        'title_page': f'Задачи {tasks.count()}',
        'all_tasks': tasks,
        'count_tasks': tasks.count(),
        'my_tasks': tasks.filter(executor=request.user),
        'my_tasks_count': tasks.filter(executor=request.user).count(),
    }
    return render(request, 'tasks/all_tasks.html', context)

def task(request, task_id):
    task = Task.objects.get(id=task_id)
    context = {'task': task,}
    return render(request, 'tasks/task.html', context)