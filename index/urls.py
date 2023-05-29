from django.urls import path

from index.views import index, catalog, hotel
from objects.views import object_detail

urlpatterns = [
    path('', index, name='index'),
    path('catalog/', catalog, name='catalog'),
    path('hotel/<object_id>/', hotel, name='hotel'),
    path('object/<slug:slug>/', object_detail, name='object_detail'),
]