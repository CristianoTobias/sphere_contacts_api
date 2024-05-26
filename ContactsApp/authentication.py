# ContactsApp/authentication.py

from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

class JWTAdminAuthenticationBackend:
    def authenticate(self, request, username=None, password=None):
        jwt_authenticator = JWTAuthentication()
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if auth_header is None:
            return None

        try:
            token = auth_header.split()[1]
            validated_token = jwt_authenticator.get_validated_token(token)
            user = jwt_authenticator.get_user(validated_token)
            if user.is_staff:
                return user
        except (AuthenticationFailed, IndexError):
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
