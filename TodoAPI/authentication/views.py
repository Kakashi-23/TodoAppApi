import jwt
from django.conf import settings
from django.contrib import auth
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import UserSerializer, LoginSerializer
from rest_framework.authtoken.models import Token


# Create your views here.

class LoginView(GenericAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        email = data.get('email', '')
        password = data.get('password', '')
        user = auth.authenticate(username=email, password=password)

        if user:
            serializer = UserSerializer(user)
            data = {'status': 'true',
                    'message': 'User Details',
                    'auth_token': user.auth_token.key,
                    'user_details': serializer.data,

                    }
            return Response(data, status=status.HTTP_200_OK)

        return Response({'status': 'false',
                         'details': 'Invalid Credentials'
                         },
                        status.HTTP_401_UNAUTHORIZED)


class RegisterUser(GenericAPIView):
    authentication_classes = ()
    permission_classes = ()
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
