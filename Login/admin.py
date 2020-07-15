
from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    fields = ['name', 'password']

admin.site.register(User, UserAdmin)