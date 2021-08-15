import jwt
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import authentication, exceptions


class JWTAuthentication(authentication.BasicAuthentication):

    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)
        print(auth_data)

        if not auth_data:
            raise exceptions.AuthenticationFailed("Invalid Token")

        prefix, token = auth_data.decode('utf-8').split(" ")

        try:
            payload = jwt.decode(token, settings.JWT_SETTINGS)
            user = User.objects.get(email=payload['username'])

            return user, token
        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed('Invalid Token')

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token Expired')

    #  return super().authenticate(request)