from models import Instagram

import requests

class Instagram:

	self.tags_url = 'https://api.instagram.com/v1/tags/%(tag)s/media/recent?'

	def __init__(self):
		logins = Instagram.objects.all()

		if logins.count!=1:
			return None

		self.client_id = logins.first().client_id

	def get_images_by_tag(self, tag):
		params = {'tag': tag}
		query_api(self.tags_url, params)


	def query_api(self, url, params):
		return requests.post(url % params)