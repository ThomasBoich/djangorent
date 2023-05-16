from django.urls import path

from index.views import index
from objects.views import object_detail

urlpatterns = [
    path('', index, name='index'),
    path('object/<slug:slug>/', object_detail, name='object_detail'),
]