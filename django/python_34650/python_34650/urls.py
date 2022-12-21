from django.contrib import admin
from django.urls import path

from python_34650.views import hola_mundo, otra_mas, fecha_actual, vista_con_edad, \
    vista_con_template, saludo_desde_template

from products.views import create_product, list_products, list_categories, create_category

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', hola_mundo, name='hola_mundo'),
    path('otra/', otra_mas),
    path('fecha/', fecha_actual),
    path('edad/<int:edad>/', vista_con_edad),
    path('vista-con-template/', vista_con_template),
    path('saludo-desde-template/', saludo_desde_template),

    path('create-product/', create_product),
    path('list-products/', list_products),

    path('create-category/<str:name>/', create_category),
    path('list-categories/', list_categories),
]
