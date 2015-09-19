from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User, related_name='profile')

	facebook_id = models.CharField(max_length=50)