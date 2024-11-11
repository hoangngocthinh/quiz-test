from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainSerializer,
    PasswordField,
    TokenObtainPairSerializer,
)
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, get_user_model

from authentication.exceptions import AuthenticateException
from user.exceptions import ObjectNotFoundException
from user.models import User
from rest_framework import exceptions
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import update_last_login


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(write_only=True, required=True)
    phone = serializers.CharField(write_only=True, required=False)
    avatar = serializers.CharField(write_only=True, required=False)
    username = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(write_only=True, required=True)
    last_name = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "first_name", "last_name", "phone", "avatar")

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    token_class = RefreshToken
    email_field = get_user_model().EMAIL_FIELD

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[self.email_field] = serializers.CharField()
        self.fields[self.username_field] = serializers.CharField(
            default=None, read_only=True, required=False
        )

    def validate(self, attrs):
        try:
            user = get_user_model().objects.get(email=attrs[self.email_field])
        except get_user_model().DoesNotExist:
            raise AuthenticateException
        authenticate_kwargs = {
            self.username_field: user.get_username(),
            "password": attrs["password"],
        }
        try:
            authenticate_kwargs["request"] = self.context["request"]
        except KeyError:
            pass
        self.user = authenticate(**authenticate_kwargs)

        if not api_settings.USER_AUTHENTICATION_RULE(self.user):
            raise exceptions.AuthenticationFailed(
                self.error_messages["no_active_account"],
                "no_active_account",
            )
        refresh = self.get_token(self.user)
        data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }
        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)
        return data
