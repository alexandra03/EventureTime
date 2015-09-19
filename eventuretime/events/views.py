from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader, Context


def index(request):
	template = loader.get_template('base.html')
	context = Context({})

	return HttpResponse(template.render(context))


def event(request):
	template = loader.get_template('event.html')
	context = Context({})

	return HttpResponse(template.render(context))

def dashboard(request):
	template = loader.get_template('dashboard.html')
	context = Context({})

	return HttpResponse(template.render(context))