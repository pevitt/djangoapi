from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Profile, Role


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'role', 'avatar', 'phone')
    search_fields = ('user__email', 'role__role_name',)

    def email(self, obj):
        return obj.user.email


@admin.register(Role)
class RolesAdmin(admin.ModelAdmin):
    list_display = ('role_name', 'role_description')
