from django.contrib import admin

from .models import Task, User
from django.contrib.auth.admin import UserAdmin

class CustomerUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_admin')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# Register your models here.
admin.site.register(User,CustomerUserAdmin)
admin.site.register(Task)