from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User

class EmailOrUsernameBackend(BaseBackend):
    """
    Custom authentication backend that allows users to log in with either their email or username.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Check if the username matches an email
            user = User.objects.get(email=username) if '@' in username else User.objects.get(username=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
