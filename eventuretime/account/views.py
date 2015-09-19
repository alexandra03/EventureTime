from django.shortcuts import render_to_response
from django.contrib.auth import login

from account.facebook_auth_backend import FacebookAuthBackend
from apis.facebook import Facebook


def authenticate(request):
	authentication = FacebookAuthBackend()

	user = authentication.authenticate(params=request.POST)

	user.backend = 'account.facebook_auth_backend.FacebookAuthBackend'

	login(request, user)

	facebook = Facebook()
	token = request.POST['params[accessToken]']
	access_token = facebook.get_access_token(token)

	#user.profile.access_token = request.POST['params[accessToken]']
	#user.profile.save()

	return render_to_response('base.html', {})