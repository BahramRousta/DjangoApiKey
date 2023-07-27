from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed
from apikey.authentication.interfaces import validate_api_key_interface


class APIKeyAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get('Api-Key')

        if not api_key:
            raise AuthenticationFailed('API key does not exist.')

        api_key = api_key.split(' ')[-1]

        try:
            validate_api_key_interface(api_key=api_key)
        except AuthenticationFailed as e:
            raise e

        return api_key, None
