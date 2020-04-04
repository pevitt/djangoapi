from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers, exceptions
from .backends import AuthenticationValidateBackend

from users.models import Profile


class AuthenticationTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):
        print("validate")
        print(data)
        email = data.get('username').lower()
        password = data.get('password')
        backend = AuthenticationValidateBackend()

        if email and password:
            user = backend.authenticate(email=email, password=password)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Must include "email" and "password".')
            raise exceptions.ValidationError(msg)

        data['user'] = user
        return data


class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    password = serializers.CharField()


    def validate_email(self, data):
        email = data.lower()

        if User.objects.filter(email=email).exists():
            msg = _("Correo ya registrado.")
            raise exceptions.ValidationError(msg)

        return email

    def validate(self, data):
        first_name = data['first_name']
        last_name = data['last_name']
        username = '%s.%s' % (first_name.lower(), last_name.lower())
        username = '{:.29}'.format(username)
        counter = User.objects.filter(first_name=first_name, last_name=last_name).count()
        if counter > 0:
            username += '%s' % (counter + 1)
        data['username'] = username
        return data
