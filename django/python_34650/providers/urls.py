from django.urls import path
from providers.views import providers_list, providers_create, provider_update

urlpatterns = [
    path('providers-list/', providers_list, name='providers_list'),
    path('provider-create/', providers_create, name='providers_create'),
    path('provider-update/<int:id>/', provider_update, name='provider_update'),
]