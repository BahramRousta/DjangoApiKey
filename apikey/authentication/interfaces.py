from django.utils import timezone
from rest_framework.exceptions import AuthenticationFailed
from apikey.authentication.use_cases.selectors import get_api_key


def validate_api_key_interface(api_key):
    api_key = get_api_key(api_key=api_key)

    if api_key is None:
        raise AuthenticationFailed('Invalid API key.')
    elif api_key.created_at <= (timezone.now() - timezone.timedelta(seconds=15)):
        raise AuthenticationFailed('API key has expired.')
    return api_key
