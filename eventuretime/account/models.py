from django.db import models
from django.dispatch.dispatcher import receiver
from django_facebook.models import FacebookModel
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django_facebook.utils import get_user_model, get_profile_model
from eventuretime import settings

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')
	profile_model = get_profile_model()

	@receiver(post_save)
	def create_profile(sender, instance, created, **kwargs):
	    """Create a matching profile whenever a user object is created."""
	    if sender == get_user_model():
	        user = instance
	        profile_model = get_profile_model()

	facebook_id = models.CharField(max_length=50, null=True, blank=True)

	access_token = models.CharField(max_length=300, null=True, blank=True)

	friends = models.ManyToManyField('self', blank=True)

	address = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.user.first_name or self.facebook_id
