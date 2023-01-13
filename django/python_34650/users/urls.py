from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import login_view

urlpatterns = [
    path('login/', login_view),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html')),
]