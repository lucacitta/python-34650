from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import login_view, register

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html')),
    path('signup/', register)
]