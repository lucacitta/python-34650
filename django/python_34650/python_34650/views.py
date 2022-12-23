from django.http import HttpResponse
from django.shortcuts import render

from datetime import datetime

def index(request):
    return render(request, 'index.html', context={})

def hola_mundo(request):
    return HttpResponse("Hola mundo")

def otra_mas(request):
    return HttpResponse('Si, otra mas...')

def fecha_actual(request):
    hoy = datetime.now().date()
    return HttpResponse(f'La fecha de hoy es {hoy}')

def vista_con_edad(request, edad):
    return HttpResponse(f'Esto funciona? la edad es {edad}?')

def vista_con_template(request):
    return render(request, 'template.html', context={})

def saludo_desde_template(request):
    context = {
        'nombre':'Luca',
        'edad':23,
        'usa_lentes':True,
        'lista_frutas': ['manzana','pera','banana','naranja'],
    }
    return render(request, 'saludo.html', context=context)