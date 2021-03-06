from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
from django.contrib.auth.decorators import login_required

from django.shortcuts import render_to_response
from django.template.context_processors import csrf

from forms import GenerateEvent
from apis.instagram import InstagramAPI
from apis.facebook import Facebook
from apis.uber import UberAPI
from events.models import Event

import indicoio
import json

def index(request):
	template = loader.get_template('base.html')
	context = Context({})

	return HttpResponse(template.render(context))


def home(request):
	template = loader.get_template('index.html')
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


def eventpage(request, event_id):
	event = Event.objects.get(pk=event_id)

	instagram = InstagramAPI()

	pictures = []
	if event.tag:
		pictures = instagram.get_images_by_tag(event.tag).json()['data']

	return render_to_response('eventpage.html', {
		'event': event,
		'pictures': pictures
	})

def new_event(request):
	user = request.user

	if request.method=='GET':
		form = GenerateEvent(user)
		results = None
	else:
		form = GenerateEvent(user, request.POST)

		if form.is_valid():
			results = form.generate(user, request.POST['longitude'], request.POST['latitude'])
		else:
			results = []
			print form.errors

	context = Context({
		'form': form,
		'results': results
	})

	context.update(csrf(request))

	return render_to_response('new_event.html', context)

def my_events(request):
	user = request.user

	events = Event.objects.filter(owner=user.profile)
	return render_to_response('event_list.html', {
		'events': events,
		'title': 'My events'
	})

def events_category(request, category):
	user = request.user
	events = Event.objects.filter(event_parts__category=category)

	return render_to_response('event_list.html', {
		'events': events,
		'title': category.title()
	})

def dashboard(request):
	template = loader.get_template('dashboard.html')
	context = Context({})

	return HttpResponse(template.render(context))

def request_uber(request, event_id):
	event = Event.objects.get(pk=event_id)
	user = request.user
	lat = user.latitude
	long = user.longitude
	server_token = user.server_token
	uber = UberAPI()

	products = uber.available_products(server_token, lat, long).json()
	product_id = products["products"][0]["product_id"]

	req_uber = uber.request(lat, long, event.latitude, event.longitude, product_id)
	# uber.update_request(req_uber["request_id"], "accepted")

	return render_to_response('eventpage.html', {
		'uber': req_uber,
	})
