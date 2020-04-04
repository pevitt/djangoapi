from rest_framework import serializers, exceptions
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from .models import Role, Profile


class UsersSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'date_joined'
        )


class RoleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    user = UsersSerializer(required=True)
    role = RoleSerializers(required=True)

    class Meta:
        model = Profile
        fields = '__all__'
