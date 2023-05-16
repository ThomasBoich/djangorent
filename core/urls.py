from django.contrib.auth import logout
from django.urls import path

from tasks.views import all_tasks
from users.views import user_info, user_profile
from .views import dash_info, LogoutView
from objects.views import all_objects, add_object

urlpatterns = [

    path('objects/', all_objects, name='objects'),
    path('add_object/', add_object, name='add_object'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', dash_info, name='dash'),
    path('user/', user_info, name='user_info'),
    path('profile/', user_profile, name='user_profile'),
    path('tasks/', all_tasks, name='tasks'),
]