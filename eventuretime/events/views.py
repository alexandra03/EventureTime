from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
from django.contrib.auth.decorators import login_required

from forms import GenerateEvent


def index(request):
	template = loader.get_template('base.html')
	context = Context({})

	return HttpResponse(template.render(context))


@login_required
def event(request):
	user = request.user

	form = GenerateEvent(user)

	template = loader.get_template('event.html')
	context = Context({
		'form': form
	})

	return HttpResponse(template.render(context))