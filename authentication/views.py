from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.tokens import default_token_generator

from .serializers import AuthenticationTokenSerializer, SignUpSerializer, serializers
# from users.serializers import UsersSerializer

from users.models import Profile

from users.selectors import UserSelector
from users.services import UserServices
from users.serializers import ProfileSerializer


# Create your views here.
class LoginView(GenericAPIView):

    def post(self, request, *args, **kwargs):
        print(request.data)
        user_serializer = AuthenticationTokenSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.validated_data['user']

        Token.objects.get_or_create(user=user)

        user_selector = UserSelector()
        profile = user_selector.get_profile_by_user(user)

        profile_data = ProfileSerializer(profile).data

        data = {'token': user.auth_token.key, 'profile': profile_data}

        return Response(data)


class SignUpView(GenericAPIView):

    def post(self, request):
        # This endpoint creates anew company and sends a confirmation email

        user_services = UserServices()
        serializer_user = SignUpSerializer(data=request.data)
        serializer_user.is_valid(raise_exception=True)
        user = user_services.create_user(serializer_user.validated_data)

        Token.objects.get_or_create(user=user)

        users_selector = UserSelector()

        role = users_selector('client')

        profile = user_services.create_profile(user, serializer_user.validated_data, role)

        profile_serializer = ProfileSerializer(profile)

        data = {'token': user.auth_token.key, 'profile': profile_serializer.data}

        return Response(data)
