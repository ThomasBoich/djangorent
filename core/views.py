from django.contrib.auth import logout
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View

from objects.models import Object, Reservation
from tasks.models import Task
from users.models import CustomUser


# Create your views here.

def dash_info(request):

    ''''
        Главная страница црм
    '''

    today = timezone.now().date()

    if request.user.is_authenticated:
        objects = Object.objects.all()
        tasks = Task.objects.all()
        orders = Reservation.objects.all()
        users = CustomUser.objects.all()
        template = 'dash/index.html'
        context = {
            'title_page': 'Dashboard',
            'count_objects': objects.count(),
            'all_clients': users.filter(type='CL').count(),
            'new_clients_today': users.filter(date_joined=today).count(),
            'all_tasks': tasks.count(),
            'tasks_in_progress': tasks.filter(status=False).count(),
            'my_tasks_in_progress': tasks.filter(Q(executor=request.user), Q(status=False)).count(),
            'all_orders': orders.count(),
            'orders_in_progress': orders.filter(Q(status_order=False), Q(manager=True), Q(status_closed=False)).count(),
            'raw_orders': orders.filter(Q(status_order=False), Q(manager=None), Q(status_closed=False)).count(),
            'finish_orders': orders.filter(status_order=True, status_closed=False).count(),
            'closed_orders': orders.filter(status_closed=True).count(),
            'back_button': False,
            'tasks': tasks.filter(status=False).order_by('-date_created')[:5],
            'reservations': orders.order_by('-created_at')[:5],
        }
        return render(request, template, context)
    else:
        return redirect("login")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")