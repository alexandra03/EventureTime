from django.db import models

from account.models import Profile

class Event(models.Model):
	'''
	Collection of EventParts to create the main overall
	event.
	'''
	owner = models.ForeignKey(Profile, related_name='events_owned')

	name = models.CharField(max_length=100, default='My new event')

	description = models.TextField()

	attending = models.ManyToManyField(Profile, related_name='events_attending')

	invited = models.ManyToManyField(Profile, related_name='events_invited_to')

	tag = models.CharField(max_length=20)

	public = models.BooleanField(default=False)

	facebook = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class EventPart(models.Model):
	'''
	One portion/leg of an Event.
	'''
	event = models.ForeignKey(Event, related_name='event_parts')

	CATEGORIES = (
		('food', 'Food'),
		('club', 'Club'),
		('movie', 'Movie'),
		('place', 'Place'),
		('other', 'Other'),
		('sports', 'Sports'),
		('concert', 'Concert'),
	)

	category = models.CharField(max_length=20, choices=CATEGORIES, default='place')


	''' Event overview data '''
	name = models.CharField(max_length=100)

	description = models.TextField()

	start = models.DateTimeField()

	end = models.DateTimeField(null=True, blank=True)


	''' Location data '''
	country = models.CharField(max_length=20)

	state = models.CharField(max_length=20)

	city = models.CharField(max_length=20)

	venue = models.CharField(max_length=50)

	latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

	longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)


	''' Other '''
	estimated_cost = models.IntegerField(default=0)


	def __str__(self):
		return self.name + ' (belongs to ' + self.event.name + ')'
