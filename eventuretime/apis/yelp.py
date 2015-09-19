import requests
import urllib
import urllib2
import oauth2
import json

from models import Yelp

class YelpAPI:

	API_HOST = 'api.yelp.com'
	SEARCH_PATH = '/v2/search/'
	BUSINESS_PATH = '/v2/business/'

	def __init__(self):
		self.credentials = Yelp.objects.all()[0]

	def request(self, host, path, url_params=None):
		url_params = url_params or {}
		url = 'http://{0}{1}?'.format(host, urllib.quote(path.encode('utf8')))

		consumer = oauth2.Consumer(self.credentials.consumer_key, self.credentials.consumer_secret)
		oauth_request = oauth2.Request(method="GET", url=url, parameters=url_params)

		oauth_request.update(
			{
				'oauth_nonce': oauth2.generate_nonce(),
				'oauth_timestamp': oauth2.generate_timestamp(),
				'oauth_token': self.credentials.token,
				'oauth_consumer_key': self.credentials.consumer_key
			}
		)

		token = oauth2.Token(self.credentials.token, self.credentials.token_secret)
		oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
		signed_url = oauth_request.to_url()

		conn = urllib2.urlopen(signed_url, None)
		try:
			response = json.loads(conn.read())
		finally:
			conn.close()

		return response


	def search(self, term, location):
		url_params = {
			'term': term.replace(' ', '+'),
			'location': location.replace(' ', '+'),
			'limit': 10
		}

		return self.request(self.API_HOST, self.SEARCH_PATH, url_params=url_params)		