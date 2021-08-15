import jwt
from django.conf import settings
from django.contrib import auth
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import UserSerializer, LoginSerializer


# Create your views here.

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    @staticmethod
    def post(request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user:
            auth_token = jwt.encode(
                {'username': user.username},
                settings.JWT_SETTINGS
            )
            serializer = UserSerializer(user)
            data = {'status': 'true',
                    'message': 'User Details',
                    'auth_token': auth_token,
                    'user_details': serializer.data,

                    }
            return Response(data, status=status.HTTP_200_OK)

        return Response({'status': 'false',
                         'details': 'Invalid Credentials'
                         },
                        status.HTTP_401_UNAUTHORIZED)


class RegisterUser(GenericAPIView):
    serializer_class = UserSerializer

    @staticmethod
    def post(request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {'status': 'true',
                 'message': 'User Registered'
                 },
                status=status.HTTP_200_OK
            )
        return Response({'status': 'false',
                         'message': serializer.errors
                         },
                        status=status.HTTP_400_BAD_REQUEST,
                        )
