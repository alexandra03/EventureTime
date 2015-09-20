from account.models import Profile
from events.models import Event, EventPart
from apis.yelp import YelpAPI
from apis.concert import Concert

from django import forms


class GenerateEvent(forms.Form):
	'''
	Collects main settings for the event collection
	'''
	date = forms.DateField(widget=forms.TextInput(attrs={'class' : 'date'}));
	
	categories = forms.ChoiceField(choices=EventPart.CATEGORIES,widget=forms.Select(attrs={'class':'categoriesDrop'}))

	date = forms.DateField()

	location = forms.CharField()

	categories = forms.MultipleChoiceField(choices=EventPart.CATEGORIES)


	invitees = forms.ModelMultipleChoiceField(Profile,widget=forms.Select(attrs={'class':'categoriesDrop'}));


	def __init__(self, user, *args, **kwargs):
		super(GenerateEvent, self).__init__(*args, **kwargs)
		self.fields['invitees'] = forms.ModelMultipleChoiceField(queryset=user.profile.friends.all())

	def generate(self, longitude=None, latitude=None):
		''' Do cool machine learning things to find events '''
		invitees = self.cleaned_data['invitees']
		location = self.cleaned_data['location']
		categories = self.cleaned_data['categories']
		date = self.cleaned_data['date']

		itinerary = []
		yelp = YelpAPI()

		if 'food' in categories:
			''' yelp! '''
			results = yelp.search('food', location)['businesses']
			place = results[0]
			event = {'name': place['name'], 'location': place['location'], 'image': place['image_url'], 'type': 'food'}

			itinerary.append(event)

			results = yelp.search('desserts', location)['businesses']
			place = results[0]
			event = {'name': place['name'], 'location': place['location'], 'image': place['image_url'], 'type': 'food'}

			itinerary.append(event)

		if 'club' in categories:
			results = yelp.search('nightlife', location)['businesses']
			place = results[0]
			event = {'name': place['name'], 'location': place['location'], 'image': place['image_url'], 'type': 'club'}

			itinerary.append(event)			

		if 'other' in categories or 'sports' in categories:
			results = yelp.search('active', location)['businesses']
			place = results[0]
			event = {'name': place['name'], 'location': place['location'], 'image': place['image_url'], 'type': 'other'}

			itinerary.append(event)	

			results = yelp.search('arts', location)['businesses']
			place = results[0]
			event = {'name': place['name'], 'location': place['location'], 'image': place['image_url'], 'type': 'other'}

			itinerary.append(event)

		if 'concert' in categories:
			concert = Concert().get_local_concerts(location, date)
			itinerary.append(concert)

		return itinerary



	def save(self, commit=True):
		instance = super(GenerateEvent, self).save(commit=False)