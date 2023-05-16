from django.urls import path

from orders.views import orders

urlpatterns = [
    path('', orders, name='orders'),
]