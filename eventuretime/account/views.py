from django.shortcuts import render_to_response
from django.contrib.auth import login

from account.facebook_auth_backend import FacebookAuthBackend
from apis.facebook import Facebook


def authenticate(request):
	authentication = FacebookAuthBackend()

	user = authentication.authenticate(facebook_id=request.POST['fb_id'])
	user.backend = 'account.facebook_auth_backend.FacebookAuthBackend'

	login(request, user)

	facebook = Facebook()
	token = request.POST['access_token']
	access_token = facebook.get_access_token(token)

	user.profile.access_token = access_token
	user.save()

	return render_to_response('base.html', {})