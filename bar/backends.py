from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class CaseInsensitiveUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            return None
        
        try:
            user = UserModel.objects.get(username__iexact=username)
        except UserModel.DoesNotExist:
            return None
        
        if user.check_password(password):
            return user
        return None

# required to accept lower - uppercase for username login