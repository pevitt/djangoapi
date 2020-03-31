from .models import Role, Profile
from django.contrib.auth.models import User


class UserSelector:

    @staticmethod
    def get_profile_by_user(user: 'User') -> 'Profile':
        profile = Profile.objects.get(user=user)

        return profile

    @staticmethod
    def get_role_by_name(role_name: 'str') -> 'Role':
        role = Role.objects.get(role_name=role_name)

        return role
