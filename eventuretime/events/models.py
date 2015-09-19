from django.db import models

from account.models import Profile

class Event(models.Model):
	'''
	Collection of EventParts to create the main overall
	event.
	'''
	owner = models.ForeignKey(Profile, related_name='events_owned')

	name = models.CharField(max_length=100)
	
	description = models.TextField()

	attending = models.ManyToManyField(Profile, related_name='events_attending')

	invited = models.ManyToManyField(Profile, related_name='events_invited_to')

	tag = models.CharField(max_length=20)

	public = models.BooleanField(default=False)

	facebook = models.CharField(max_length=100)


class EventPart(models.Model):
	'''
	One portion/leg of an Event.
	'''
	event = models.ForeignKey(Event, related_name='event')

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

	end = models.DateTimeField()


	''' Location data '''
	country = models.CharField(max_length=20)

	state = models.CharField(max_length=20)

	city = models.CharField(max_length=20)

	venue = models.CharField(max_length=50)


	''' Other '''
	estimated_cost = models.IntegerField()




