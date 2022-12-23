from django.urls import path

from orders.views import list_orders, create_order

urlpatterns = [
    path('list-orders/', list_orders),
    path('create-order/', create_order),
]