from django.db import models
from django.contrib.auth.models import User
from eventuretime import settings

class Profile(models.Model):
	user = models.OneToOneField(User, related_name='profile')

	facebook_id = models.CharField(max_length=50, null=True, blank=True)

	access_token = models.CharField(max_length=300, null=True, blank=True)

	friends = models.ManyToManyField('self', blank=True)

	def __str__(self):
		return self.user.first_name or self.facebook_id