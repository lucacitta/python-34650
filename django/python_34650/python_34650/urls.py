from django.contrib import admin
from django.urls import path, include

from python_34650.views import hola_mundo, otra_mas, fecha_actual, vista_con_edad, \
    vista_con_template, saludo_desde_template, index


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('hola/', hola_mundo, name='hola_mundo'),
    path('otra/', otra_mas),
    path('fecha/', fecha_actual),
    path('edad/<int:edad>/', vista_con_edad),
    path('vista-con-template/', vista_con_template),
    path('saludo-desde-template/', saludo_desde_template),

    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
    path('providers/', include('providers.urls')),
    path('users/', include('users.urls')),
    
]
