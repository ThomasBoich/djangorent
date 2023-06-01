from django.urls import path

from index.views import index, catalog, hotel, about, contacts

urlpatterns = [
    path('', index, name='index'),
    path('catalog/', catalog, name='catalog'),
    path('hotel/<object_id>/', hotel, name='hotel'),
    path('contacts/', contacts, name='contacts'),
    path('about/', about, name='about'),
]