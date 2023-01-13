from django import forms

from providers.models import Provider

class ProviderForm(forms.Form):
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=300)
    phone_number = forms.CharField(max_length=20)
    email = forms.EmailField()
    condition = forms.CharField(max_length=50)

# class ProviderForm(forms.ModelForm):
#     class Meta:
#         model = Provider
#         fields = '__all__'
