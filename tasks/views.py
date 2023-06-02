from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

from .forms import TaskCommentForm, addTaskForm
from tasks.models import Task
from objects.models import Object, Reservation


# Create your views here.

def all_tasks(request):
    tasks = Task.objects.all()
    context = {
        'active': 'active',
        'title_page': f'Tasks {tasks.count()}',
        'all_tasks': tasks,
        'count_tasks': tasks.count(),
        'my_tasks': tasks.filter(Q(executor=request.user), Q(status=False)),
        'my_tasks_count': tasks.filter(Q(executor=request.user), Q(status=False)).count(),
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

    context = {'task': task,'back_button': True, 'form': form, 'title_page': f'{task.title}', 'objects': Object.objects.all(), 'reservation': Reservation.objects.all(),}
    return render(request, 'tasks/task.html', context)

def task_done(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.status == True:
        task.status = False
        task.save()
        return redirect('task', task_id=task_id)
    else:
        task.status = True
        task.save()
        return redirect('task', task_id=task_id)

def task_reservation_done(request, task_id, reservation_id):
    task = Task.objects.get(id=task_id)
    reservation = Reservation.objects.get(id=reservation_id)
    if task.status == True:
        task.status = False
        task.save()
        return redirect('tasks_reservation', reservation_id=reservation_id)
    else:
        task.status = True
        task.save()
        return redirect('tasks_reservation', reservation_id=reservation_id)

def new_task(request):
    if request.user.is_authenticated == True:
        if request.method == 'POST':
                form = addTaskForm(request.POST, request.FILES)
                if form.is_valid():
                    new_task = form.save(commit=False)
                    new_task.save()
                    return redirect('tasks')
        else:
            form = addTaskForm()
            context = {'form': form, 'active': 'active', 'title_page': 'Adding an task'}
            return render(request, 'tasks/create_task.html', context)
    else:
        return redirect('/')
