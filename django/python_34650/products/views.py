from django.shortcuts import render
from django.http import HttpResponse

from products.models import Products

# Create your views here.
def create_product(request):
    new_product = Products.objects.create(name='Coca cola 1L', price=250, stock=False)
    print(new_product)
    return HttpResponse('Se creo el nuevo producto')

def list_products(request):
    all_products = Products.objects.all()
    print(all_products)
    context = {
        'products':all_products,
    }
    return render(request, 'list_products.html', context=context)