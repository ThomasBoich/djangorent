from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import TaskCommentForm
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
        'back_button': False,
    }
    return render(request, 'tasks/all_tasks.html', context)

@login_required
def task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.task = task
            comment.save()
            return redirect('task', task_id=task_id)
    else:
        form = TaskCommentForm()

    context = {'task': task,'back_button': True, 'form': form, 'title_page': f'{task.title}'}
    return render(request, 'tasks/task.html', context)