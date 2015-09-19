from django.db import models
from django.dispatch.dispatcher import receiver
from django_facebook.models import FacebookModel
from django.db.models.signals import post_save
from django_facebook.utils import get_user_model, get_profile_model
from eventuretime import settings

class Profile(FacebookModel):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')
	profile_model = get_profile_model()

	@receiver(post_save)
	def create_profile(sender, instance, created, **kwargs):
	    """Create a matching profile whenever a user object is created."""
	    if sender == get_user_model():
	        user = instance
	        profile_model = get_profile_model()

	    # if profile_model == Profile and created:
	    #     profile, new = Profile.objects.get_or_create(user=instance)

	# def __str__(self):
	# 	return self.user.first_name + ' ' + self.user.last_name

# class Profile(FacebookModel):
# 	user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')
#
# 	facebook_id = models.CharField(max_length=50)
#
# 	friends = models.ManyToManyField('self', blank=True)
#
# 	def __str__(self):
# 		return self.user.first_name + ' ' + self.user.last_name
