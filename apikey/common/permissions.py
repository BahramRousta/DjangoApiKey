from django.core.exceptions import ObjectDoesNotExist
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed
from apikey.authentication.interfaces import validate_api_key_interface


class APIKeyAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        print(request.headers)
        api_key = request.headers.get('Api-Key')

        if not api_key:
            raise AuthenticationFailed('API key does not exist.')

        api_key = api_key.split(' ')[-1]

        try:
            api_key = validate_api_key_interface(api_key=api_key)
        except ObjectDoesNotExist:
            raise AuthenticationFailed('Invalid API key.')

        return api_key, None
