from rest_framework.exceptions import AuthenticationFailed
from apikey.authentication.use_cases.selectors import get_api_key


def validate_api_key_interface(api_key):
    api_key = get_api_key(api_key=api_key)
    if api_key is None:
        raise AuthenticationFailed('Invalid API key.')
    return api_key
