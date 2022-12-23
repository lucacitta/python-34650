from django.urls import path

from products.views import create_product, list_products, list_categories, create_category


urlpatterns = [
    path('create-product/', create_product),
    path('list-products/', list_products),

    path('create-category/<str:name>/', create_category),
    path('list-categories/', list_categories),
]