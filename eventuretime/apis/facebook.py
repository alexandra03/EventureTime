import urllib
import urlparse
import requests

from django.conf import settings

class Facebook:
	BASE_URL = 'https://graph.facebook.com'

	def get_access_token(self, token):
		path = '/oauth/access_token?'

		params = {
			'grant_type': 'fb_exchange_token',        
			'client_id': settings.FACEBOOK_APP_ID,
			'client_secret': settings.FACEBOOK_APP_SECRET,
			'redirect_uri': 'http://localhost:8000/event',
			'fb_exchange_token': token	
		}

		return self.query_api(path, params)

	def query_api(self, path, params):
		url = self.BASE_URL+path

		url_parts = list(urlparse.urlparse(url))
		query = dict(urlparse.parse_qsl(url_parts[4]))
		query.update(params)

		url_parts[4] = urllib.urlencode(query)

		response = requests.get(urlparse.urlunparse(url_parts))

		return response
		return response.json()['data']['access_token']