from account.models import Profile
from events.models import Event, EventPart

from django import forms


class GenerateEvent(forms.Form):
	'''
	Collects main settings for the event collection
	'''
	categories = forms.MultipleChoiceField(choices=EventPart.CATEGORIES)

	start = forms.DateTimeField()

	country = forms.CharField(max_length=20)

	state = forms.CharField(max_length=20)

	city = forms.CharField(max_length=20)

	invitees = forms.ModelMultipleChoiceField(Profile)


	def __init__(self, user, *args, **kwargs):
		super(GenerateEvent, self).__init__(*args, **kwargs)
		self.fields['invitees'] = forms.ModelMultipleChoiceField(queryset=user.profile.friends.all())

	def generate(self):
		''' Do cool machine learning things to find events '''

	def save(self, commit=True):
		instance = super(GenerateEvent, self).save(commit=False)