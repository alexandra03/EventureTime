from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

from account.models import Profile

class FacebookAuthBackend(ModelBackend):
    ''' Log in to django with Facebook and not user password '''

    def authenticate(self, facebook_id=None):
        try:
            return Profile.objects.get(facebook_id=facebook_id).user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Profile.objects.get(facebook_id=user_id).user
        except User.DoesNotExist:
            return None