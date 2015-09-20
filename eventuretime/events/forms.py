from account.models import Profile
from events.models import Event, EventPart
from apis.yelp import YelpAPI
from apis.concert import Concert

from django import forms

import random
random.seed()


class GenerateEvent(forms.Form):
	'''
	Collects main settings for the event collection
	'''
	date = forms.DateField(widget=forms.TextInput(attrs={'class' : 'date'}));

	location = forms.CharField()

	categories = forms.MultipleChoiceField(choices=EventPart.CATEGORIES)

	invitees = forms.ModelMultipleChoiceField(Profile,widget=forms.Select(attrs={'class':'categoriesDrop'}));


	def __init__(self, user, *args, **kwargs):
		super(GenerateEvent, self).__init__(*args, **kwargs)
		self.fields['invitees'] = forms.ModelMultipleChoiceField(queryset=user.profile.friends.all())

	def generate(self, owner, longitude=None, latitude=None):
		invitees = self.cleaned_data['invitees']
		location = self.cleaned_data['location']
		categories = self.cleaned_data['categories']
		date = self.cleaned_data['date']

		main_event = Event.objects.create(owner=owner.profile, public=False)
		main_event.save()
		for person in invitees:
			main_event.invited.add(person)
		main_event.save()

		itinerary = []
		yelp = YelpAPI()

		if 'food' in categories:
			results = yelp.search('food', location)['businesses']
			num = random.randint(0, len(results)-1)
			place = results[num]
			event = {'name': place['name'], 'location': place['location'], 'image': place.get('image_url', ''), 'type': 'food'}
			event_part = EventPart.objects.create(
				name=place['name'],
				city=place['location']['city'],
				category='food',
				event=main_event,
				start=date,
				end=date
			)
			event_part.save()
			itinerary.append(event)

			results = yelp.search('desserts', location)['businesses']
			num = random.randint(0, len(results)-1)			
			place = results[num]
			event = {'name': place['name'], 'location': place['location'], 'image':  place.get('image_url', ''), 'type': 'food'}

			itinerary.append(event)

		if 'club' in categories:
			results = yelp.search('nightlife', location)['businesses']
			num = random.randint(0, len(results)-1)
			place = results[num]
			event = {'name': place['name'], 'location': place['location'], 'image':  place.get('image_url', ''), 'type': 'club'}
			event_part = EventPart.objects.create(
				name=place['name'],
				city=place['location']['city'],
				category='club',
				event=main_event,
				start=date,
				end=date
			)
			event_part.save()
			itinerary.append(event)			

		if 'other' in categories or 'sports' in categories:
			results = yelp.search('active', location)['businesses']
			num = random.randint(0, len(results)-1)
			place = results[num]
			event = {'name': place['name'], 'location': place['location'], 'image':  place.get('image_url', ''), 'type': 'other'}
			event_part = EventPart.objects.create(
				name=place['name'],
				city=place['location']['city'],
				category='other',
				event=main_event,
				start=date,
				end=date
			)
			event_part.save()
			itinerary.append(event)	

			results = yelp.search('arts', location)['businesses']
			num = random.randint(0, len(results)-1)
			place = results[num]
			event = {'name': place['name'], 'location': place['location'], 'image':  place.get('image_url', ''), 'type': 'other'}

			itinerary.append(event)

		if 'concert' in categories:
			concert = Concert().get_local_concerts(location, date)
			itinerary.append(concert)
			event_part = EventPart.objects.create(
				name=concert['name'],
				city=concert['location'],
				category='concert',
				event=main_event,
				start=date,
				end=date
			)
			event_part.save()
		return itinerary



	def save(self, commit=True):
		instance = super(GenerateEvent, self).save(commit=False)