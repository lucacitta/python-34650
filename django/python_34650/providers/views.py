from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from providers.models import Provider
from providers.forms import ProviderForm

def providers_list(request):
    providers = Provider.objects.filter(is_active = True)
    context = {
        'providers':providers
    }
    return render(request, 'providers/providers-list.html', context=context)

class ProvidersListView(LoginRequiredMixin, ListView):
    model = Provider
    template_name = 'providers/providers-list.html'
    queryset = Provider.objects.filter(is_active = True)







def providers_create(request):
    if request.method == 'GET':
        context = {
            'form': ProviderForm()
        }

        return render(request, 'providers/provider-create.html', context=context)

    elif request.method == 'POST':
        form = ProviderForm(request.POST)
        if form.is_valid():
            Provider.objects.create(
                name = form.cleaned_data['name'],
                address = form.cleaned_data['address'],
                phone_number = form.cleaned_data['phone_number'],
                email = form.cleaned_data['email'],
                condition = form.cleaned_data['condition'],
            )
            context = {
                'message': 'Proveedor creado exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': ProviderForm()
            }
        return render(request, 'providers/provider-create.html', context=context)

class ProviderCreateView(CreateView):
    model = Provider
    template_name = 'providers/provider-create.html'
    fields = '__all__'
    success_url = '/providers/providers-list/'






def provider_update(request, pk):
    provider = Provider.objects.get(id=pk)

    if request.method == 'GET':
        context = {
            'form': ProviderForm(
                initial={
                    'name':provider.name,
                    'address':provider.address,
                    'phone_number':provider.phone_number,
                    'email':provider.email,
                    'condition':provider.condition,
                }
            )
        }

        return render(request, 'providers/provider-update.html', context=context)

    elif request.method == 'POST':
        form = ProviderForm(request.POST)
        if form.is_valid():
            provider.name = form.cleaned_data['name']
            provider.address = form.cleaned_data['address']
            provider.phone_number = form.cleaned_data['phone_number']
            provider.email = form.cleaned_data['email']
            provider.condition = form.cleaned_data['condition']
            provider.save()
            
            context = {
                'message': 'Proveedor actualizado exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': ProviderForm()
            }
        return render(request, 'providers/provider-update.html', context=context)

# class ProviderUpdateView(UpdateView)




# def provider_delete(request, pk):     //provider.delete()

class ProviderDeleteView(DeleteView):
    model = Provider
    template_name = 'providers/provider-delete.html'
    success_url = '/providers/providers-list/'

