from django.contrib.auth import logout
from django.urls import path

from tasks.views import all_tasks, task, task_done, task_reservation_done, new_task
from users.views import user_info#, user_profile
from .views import dash_info, LogoutView
from objects.views import all_objects, add_object, reservation_list, reservation, tasks_reservation, EditNote

urlpatterns = [

    path('objects/', all_objects, name='objects'),
    path('add_object/', add_object, name='add_object'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', dash_info, name='dash'),
    path('user/<user_id>', user_info, name='user_info'),
    # path('profile/', user_profile, name='user_profile'),
    path('tasks/', all_tasks, name='tasks'),
    path('task/<task_id>/', task, name='task'),
    path('new_task/', new_task, name='new_task'),
    path('reservations/', reservation_list, name='reservations'),
    path('reservation/<int:reservation_id>/', reservation, name='reservation'),
    path('task_done/<task_id>/', task_done, name='task_done'),
    path('reservation/tasks/<reservation_id>', tasks_reservation, name='tasks_reservation'),
    path('reservation/tasks/<int:task_id>/<int:reservation_id>/', task_reservation_done, name='task_reservation_done'),
    path('object/<int:object_id>/', EditNote.as_view(), name='object_info'),
]