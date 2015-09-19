from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context

from forms import GenerateEvent


def index(request):
	template = loader.get_template('base.html')
	context = Context({})

	return HttpResponse(template.render(context))


def event(request):
	form = GenerateEvent('a')

	template = loader.get_template('event.html')
	context = Context({
		'form': form
	})

	return HttpResponse(template.render(context))