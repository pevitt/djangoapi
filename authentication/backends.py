from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend


class AuthenticationValidateBackend():

    def authenticate(self, email=None, password=None, **kwargs):
        if email is None:
            email = kwargs.get('email')
        try:
            user = User.objects.get(email=email)
            print('USER', user)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None