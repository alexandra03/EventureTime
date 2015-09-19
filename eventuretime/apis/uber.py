from models import Uber
from rauth import OAuth2Service
from time import sleep

import requests

class UberAPI:

    API_HOST = 'https://api.uber.com'
    SANDBOX_HOST = 'https://sandbox-api.uber.com'

    # paths that don't require OAuth
    PRODUCTS_PATH = '/v1/products'
    TIME_ESTIMATE_PATH = '/v1/estimates/time'
    PRICE_ESTIMATE_PATH = '/v1/estimates/price'

    # paths that require OAuth
    USER_INFO_PATH = '/v1/me'
    SANDBOX_REQUEST_PATH = '/v1/sandbox/requests'

    def __init__(self):
        self.credentials = Uber.objects.all()[0]
        authenticate()

    def authenticate(self):
        uber_api = OAuth2Service(
            client_id = self.credentials.client_id,
            client_secret = self.credentials.client_secret,
            name = 'EventureTime',
            authorize_url = 'https://login.uber.com/oauth/authorize',
            access_token_url = 'https://login.uber.com/oauth/token',
            base_url = 'https://api.uber.com/v1/',
        )

        parameters = {
            'response_type': 'code',
            'redirect_uri': login_url,
            'scope': 'profile',
        }

        # Redirect user here to authorize your application
        login_url = uber_api.get_authorize_url(**parameters)

        parameters = {
            'redirect_uri': login_url,
            'code': request.args.get('code'),
            'grant_type': 'authorization_code',
        }

        response = requests.post(
            'https://login.uber.com/oauth/token',
            auth=(
                self.credentials.client_id,
                self.credentials.client_secret,
            ),
            data=parameters,
        )

        # This access_token is what we'll use to make requests in the following
        # steps
        self.access_token = response.json().get('access_token')

    def available_products(self, server_token, latitude, longitude):
        url = API_HOST + PRODUCTS_PATH

        parameters = {
            'server_token': server_token,
            'latitude': latitude,
            'longitude': longitude,
        }

        response = requests.get(url, params=parameters)
        # data = response.json()

        return response

    def time_estimate(self, start_latitude, start_longitude, product_id):
        url = API_HOST + TIME_ESTIMATE_PATH

        parameters = {
            'start_latitude': start_latitude,
            'start_longitude': start_longitude,
            'product_id': product_id,
        }

        response = requests.get(url, params=parameters)
        # data = response.json()

        return response

    def price_estimate(self, start_latitude, start_longitude, end_latitude, end_longitude):
        url = API_HOST + PRICE_ESTIMATE_PATH

        parameters = {
            'start_latitude': start_latitude,
            'start_longitude': start_longitude,
            'end_latitude': end_latitude,
            'end_longitude': end_longitude,
        }

        response = requests.get(url, params=parameters)
        # data = response.json()

        return response

    def user_info(self):
        url = API_HOST + USER_INFO_PATH
        response = requests.get(
            url,
            headers={
                'Authorization': 'Bearer %s' % self.access_token
            }
        )
        # data = response.json()

        return response

    def request(self, start_latitude, start_longitude, end_latitude, end_longitude, product_id):
        url = SANDBOX_HOST + SANDBOX_REQUEST_PATH

        parameters = {
            'start_latitude': start_latitude,
            'start_longitude': start_longitude,
            'end_latitude': end_latitude,
            'end_longitude': end_longitude,
            'product_id': product_id,
        }

        response = requests.post(
            url,
            headers = {
                'Authorization': 'Bearer %s' % self.access_token
            },
            params=parameters
        )

        while response["status"] not in ('completed', 'driver_canceled', 'rider_canceled'):
            response = requests.get(
                url + '/' + response["request_id"],
                headers = {
                    'Authorization': 'Bearer %s' % self.access_token
                }
            )

            # delay between GET requests for ride status updates
            sleep(3)


        return response

    def cancel_request(self, request_id):
        url = SANDBOX_HOST + SANDBOX_REQUEST_PATH + '/' + request_id

        response = requests.delete(
            url,
            headers = {
                'Authorization': 'Bearer %s' % self.access_token
            }
        )

        return response
