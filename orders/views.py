from django.shortcuts import render

# Create your views here.

def orders(request):
    orders = Order.objects.all()
    context = {
        'title_page': f'Заказы {orders}',
    }
    return render(request, 'orders/orders.html', context)