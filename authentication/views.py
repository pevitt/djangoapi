from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.tokens import default_token_generator

from .serializers import AuthenticationTokenSerializer, SignUpSerializer, serializers

from users.models import Profile

from users.selectors import UserSelector
from users.serializers import ProfileSerializer


# Create your views here.
class LoginView(GenericAPIView):

    def post(self, request, *args, **kwargs):
        user_serializer = serializers.AuthenticationTokenSerializer(data=request.data)
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

        auth_utils = AuthenticationUtils()
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = auth_utils.create_user(serializer.validated_data)
        Token.objects.get_or_create(user=user)
        profile = auth_utils.create_profile(user, serializer.validated_data, False)
        auth_utils.create_permissions(profile)
        auth_utils.create_notifications(profile)


        return Response({'user': profile_data})
