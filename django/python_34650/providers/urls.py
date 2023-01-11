from django.urls import path
from providers.views import providers_list, providers_create, provider_update, ProvidersListView, \
    ProviderCreateView, ProviderDeleteView

urlpatterns = [
    path('providers-list/', ProvidersListView.as_view(), name='providers_list'),
    path('provider-create/', ProviderCreateView.as_view(), name='providers_create'),
    path('provider-update/<int:pk>/', provider_update, name='provider_update'),
    path('provider-delete/<int:pk>/', ProviderDeleteView.as_view(), name='provider_delete'),

]