from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from users.models import UserProfile
from django import forms




class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True, label='Nombre')
    last_name = forms.CharField(max_length=100, required=True, label='Apellido')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, label='Nombre de usuario')
    first_name = forms.CharField(max_length=100, required=True, label='Nombre')
    last_name = forms.CharField(max_length=100, required=True, label='Apellido')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'birth_date', 'profile_picture']