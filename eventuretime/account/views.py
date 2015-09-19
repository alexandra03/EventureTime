from django.shortcuts import render_to_response
from account.facebook_auth_backend import FacebookAuthBackend
from django.contrib.auth import login

def authenticate(request):
	authentication = FacebookAuthBackend()

	user = authentication.authenticate(facebook_id=request.POST['fb_id'])
	user.backend = 'account.facebook_auth_backend.FacebookAuthBackend'

	login(request, user)

	return render_to_response('base.html', {})