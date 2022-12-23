from django.shortcuts import render
from django.http import HttpResponse

from orders.models import Order

def list_orders(request):
    orders = Order.objects.all()
    context = {
        'orders': orders,
    }
    return render(request, 'orders/list_orders.html', context=context)

def create_order(request):
    Order.objects.create(client='Franco', product='Curso Python', payment_method='Card')
    return HttpResponse('Order created')

