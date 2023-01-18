from django.contrib import admin
from users.models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('phone', 'birth_date')
