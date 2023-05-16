from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from objects.models import Object


# Create your views here.
def dash_info(request):
    if request.user.is_authenticated:
        objects = Object.objects.all()
        template = 'dash/index.html'
        context = {'title_page': 'Рабочий стол', 'count_objects': objects.count(), 'all_clients': 0, 'new_clients_today': 0,
                   'all_tasks': 0, 'tasks_in_progress': 0, 'all_orders': 0, 'orders_in_progress': 0, 'raw_orders': 0, 'finish_orders': 0,}
        return render(request, template, context)
        # return render(request, 'objects/index.html', context=context)
    else:
        return redirect("login")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")