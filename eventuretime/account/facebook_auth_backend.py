from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

from account.models import Profile

import random
import string 

def create_new_user(params):
    def random_string(num):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(num))

    user = User.objects.create_user(random_string(10), '', random_string(20))
    user.save()

    Profile.objects.create(user=user, facebook_id=params['params[userID]'])

    return user

class FacebookAuthBackend(ModelBackend):
    ''' Log in to django with Facebook and not user password '''

    def authenticate(self, params=None):
        try:
            return Profile.objects.get(facebook_id=params['params[userID]']).user
        except Profile.DoesNotExist:
            return create_new_user(params)

    def get_user(self, user_id):
        try:
            return Profile.objects.get(facebook_id=user_id).user
        except Profile.DoesNotExist:
            return None