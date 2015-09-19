import urllib
import urlparse

from eventuretime import settings

class Facebook:
	BASE_URL = 'https://graph.facebook.com'

	def get_access_token(self, token):
		path = '/oauth/access_token?'

		params = {
			'grant_type': 'fb_exchange_token',        
			'client_id': settings.FACEBOOK_APP_ID,
			'client_secret': settings.FACEBOOK_APP_SECRET,
			'fb_exchange_token': token	
		}

		return self.query_api(paht, params)

	def query_api(self, path, params):
		url = self.BASE_URL+path

		url_parts = list(urlparse.urlparse(url))
		query = dict(urlparse.parse_qsl(url_parts[4]))
		query.update(params)

		url_parts[4] = urllib.urlencode(query)

		return requests.post(urlparse.urlunparse(url_parts))