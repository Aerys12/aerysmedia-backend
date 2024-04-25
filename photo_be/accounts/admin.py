from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = ['username', 'email', 'bio', 'website_url', 'is_staff']

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio', 'profile_picture', 'website_url')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('bio', 'profile_picture', 'website_url')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

