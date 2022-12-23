from django.shortcuts import render
from django.http import HttpResponse

from products.models import Products, Category

def create_product(request):
    new_product = Products.objects.create(name='Coca cola 1L', price=250, stock=False)
    print(new_product)
    return HttpResponse('Se creo el nuevo producto')

def list_products(request):
    all_products = Products.objects.all()
    context = {
        'products':all_products,
    }
    return render(request, 'products/list_products.html', context=context)

def create_category(request, name):
    Category.objects.create(name=name)
    return HttpResponse('Categoria creada')

def list_categories(request):
    all_categories = Category.objects.all()
    context = {
        'categories':all_categories
    }
    return render(request, 'categories/list_categories.html', context=context)

