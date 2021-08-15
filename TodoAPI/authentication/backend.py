from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend, UserModel
from django.core.exceptions import MultipleObjectsReturned
from django.db.models import Q


# class JWTAuthentication(authentication.BasicAuthentication):
#
#     def authenticate(self, request):
#         auth_data = authentication.get_authorization_header(request)
#         print(auth_data)
#
#         if not auth_data:
#             raise exceptions.AuthenticationFailed("Invalid Token")
#
#         prefix, token = auth_data.decode('utf-8').split(' ')
#
#         try:
#             payload = jwt.decode(token, settings.JWT_SETTINGS)
#             user = User.objects.get(username=payload['email'])
#
#             return user, token
#         except jwt.DecodeError:
#             raise exceptions.AuthenticationFailed('Invalid Token')
#
#         except jwt.ExpiredSignatureError:
#             raise exceptions.AuthenticationFailed('Token Expired')
#
#         return super().authenticate(request)

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:  # to allow authentication through phone number or any other field, modify the below statement
            user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        except MultipleObjectsReturned:
            return User.objects.filter(email=username).order_by('id').first()
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

    def get_user(self, user_id):
        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None

        return user if self.user_can_authenticate(user) else None
