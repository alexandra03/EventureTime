from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User, related_name='profile')

	facebook_id = models.CharField(max_length=50)

	friends = models.ManyToManyField('self', blank=True)

	def __str__(self):
		return self.user.first_name + ' ' + self.user.last_name