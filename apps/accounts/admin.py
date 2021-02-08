from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'first_name', 'last_name', 'ext')
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
