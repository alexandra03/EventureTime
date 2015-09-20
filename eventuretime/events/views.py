from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
from django.contrib.auth.decorators import login_required

from django.shortcuts import render_to_response
from django.template.context_processors import csrf

from events.forms import GenerateEvent
from events.models import EventPart
from apis.instagram import InstagramAPI
from apis.uber import UberAPI
from apis.facebook import Facebook

from geolocation.google_maps import GoogleMaps

import indicoio

def index(request):
	template = loader.get_template('base.html')
	context = Context({})

	return HttpResponse(template.render(context))


def login(request):
	context = {}
	context.update(csrf(request))

	return render_to_response('login.html', context)


def event(request):
	user = request.user

	if request.method=='GET':
		form = GenerateEvent(user)
		results = None
	else:
		form = GenerateEvent(user, request.POST)

		results = ['event1', 'event2']

	instagram = InstagramAPI()

	response = instagram.get_images_by_tag('tech').json()['data']

	context = Context({
		'form': form,
		'results': results,
		'pictures': response,
	})

	context.update(csrf(request))

	return render_to_response('event.html', context)

def new_event(request):
	user = request.user

	if request.method=='GET':
		form = GenerateEvent(user)
		results = None
	else:
		form = GenerateEvent(user, request.POST)
		results = ['event1', 'event2']

	context = Context({
		'form': form,
		'results': results
	})

	context.update(csrf(request))

	return render_to_response('new_event.html', context)

def dashboard(request):
	template = loader.get_template('dashboard.html')
	context = Context({})

	return HttpResponse(template.render(context))

def near_user(request):
	user = request.user
	address = user.address

	# google_maps = GoogleMaps(api_key='AIzaSyAHGsBgxTJMynBui8pOsTdz018HsEagHCg')

	if request.method == 'GET':
		form = GenerateEvent(user)
		results = form.generate(address=address)
	else:
		form = GenerateEvent(user, request.POST)
		results = ['event1', 'event2']

	context = Context({
		'form': form,
		'results': results,
	})

	context.update(csrf(request))

	return render_to_response('event.html', context)

def list_categories(request):
	category = request.category
	categories = EventPart.objects.get(category=category)

	context = Context({
		'results': categories,
	})

	context.update(csrf(request))

	return render_to_response('event.html', context)

def recommended_events(request):
	user = request.user
	data = Facebook()
	events_path = '/v2.4/me'
	params = {
	    'fields': ['events'],
	    'access_token': user.access_token,
	}

	ml_data = data.query_api(events_path, params)

	indicoio.config.api_key = 'f400ceccb73c9d2d55e5744a17c11f8d'
	key_words = []

	for description in ml_data["events"]["data"]["description"]:
	    key_words += indicoio.keywords(description)

	for name in ml_data["events"]["data"]["name"]:
	    key_words += indicoio.keywords(name)

	# filter events by keywords
	possible_events = {}
	for keyword in key_words:
	    possible_events += Event.objects.filter(keyword in name)
	    possible_events += Event.objects.filter(keyword in description)

	context = Context({
		'results': possible_events,
	})

	context.update(csrf(request))

	return render_to_response('event.html', context)
