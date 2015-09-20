from account.models import Profile
from events.models import Event, EventPart
from apis.yelp import YelpAPI

from django import forms


class GenerateEvent(forms.Form):
	'''
	Collects main settings for the event collection
	'''
	date = forms.DateField()

	location = forms.CharField()

	categories = forms.MultipleChoiceField(choices=EventPart.CATEGORIES)

	invitees = forms.ModelMultipleChoiceField(Profile)


	def __init__(self, user, *args, **kwargs):
		super(GenerateEvent, self).__init__(*args, **kwargs)
		self.fields['invitees'] = forms.ModelMultipleChoiceField(queryset=user.profile.friends.all())

	def generate(self, longitude=None, latitude=None):
		''' Do cool machine learning things to find events '''
		invitees = self.cleaned_data['invitees']
		location = self.cleaned_data['location']
		categories = self.cleaned_data['categories']
		date = self.cleaned_data['date']

		if 'food' in categories:
			''' yelp! '''
			yelp = YelpAPI()
			results = yelp.search('food', location)
			print results



	def save(self, commit=True):
		instance = super(GenerateEvent, self).save(commit=False)