from models import Instagram

import requests

class InstagramAPI:

	def get_images_by_tag(self, tag):
		logins = Instagram.objects.all()

		if logins.count()!=1:
			return None

		client_id = logins.first().client_id

		params = {
			'tag': tag, 
			'client_id': client_id
		}

		tags_url = 'https://api.instagram.com/v1/tags/%(tag)s/media/recent?client_id=%(client_id)s'

		url = tags_url%params

		return requests.get(url)