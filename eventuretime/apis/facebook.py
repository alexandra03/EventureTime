import urllib.parse as uparse
import requests
import json

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
		url_parts = list(uparse.urlparse(url))

		query = dict(uparse.parse_qsl(url_parts[4]))
		query.update(params)

		url_parts[4] = uparse.urlencode(query)

		response = requests.get(uparse.urlunparse(url_parts))
		response = json.loads(response.text)

		ml_data = {}
		next = response["events"]["data"]["next"]

		while next != None:
			for resp in response:
				ml_data["events"]["data"]["description"] = response["events"]["data"]["description"]
				ml_data["events"]["data"]["name"] = response["events"]["data"]["name"]

			response = json.loads(requests.get(next).text)

		# import ipdb
		# ipdb.set_trace()
		return ml_data
