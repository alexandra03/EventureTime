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

	invitees = forms.ModelChoiceField(Profile)


	def __init__(self, user, *args, **kwargs):
		super(GenerateEvent, self).__init__(*args, **kwargs)
		self.fields['invitees'] = forms.ModelChoiceField(queryset=Profile.objects.all())

	def save(self, commit=True):
		instance = super(GenerateEvent, self).save(commit=False)