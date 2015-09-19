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


def event(request):
	user = request.user

	if request.method=='GET':
		form = GenerateEvent(user)
		results = None
	else:
		form = GenerateEvent(user, request.POST)
		print form.is_valid()
		print form.errors
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
>>>>>>> amber-de
