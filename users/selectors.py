from .models import Role, Profile
from django.contrib.auth.models import User


class UserSelector:

    @staticmethod
    def get_profile_by_user(user: 'User') -> 'Profile':
        profile = Profile.objects.get(user=user)

        return profile
