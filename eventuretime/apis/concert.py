import requests

class Concert:

	BASE_URL = 'http://api.bandsintown.com/events/search'

	def get_local_concerts(self, location, date):
		params = {
			'location': location,
			'date': date,
			'app_id': 'eventuretime'
		}

		url = self.BASE_URL + '?location=%(location)s&date=%(date)s&app_id=%(app_id)s&format=json' % params
		response = requests.get(url).json()

		if not len(response):
			return {}

		itinerary = {
			'name': response[0]['artists'][0]['name'],
			'location': response[0]['venue']['name'],
			'url': response[0]['ticket_url'],
			'type': 'concert'
		}

		return itinerary