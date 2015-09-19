from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
from django.contrib.auth.decorators import login_required

from django.shortcuts import render_to_response
from django.template.context_processors import csrf

from forms import GenerateEvent


def index(request):
	template = loader.get_template('base.html')
	context = Context({})

	return HttpResponse(template.render(context))


def login(request):
	context = {}
	context.update(csrf(request))

	return render_to_response('login.html', context)

#@login_required
def event(request):
	user = request.user

	form = GenerateEvent(user)

	context = Context({
		'form': form
	})

	return render_to_response('new_event.html', context)
