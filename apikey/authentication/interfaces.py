from apikey.authentication.use_cases.selectors import get_api_key


def validate_api_key_interface(api_key):

    api_key = get_api_key(api_key=api_key)
    if not api_key:
        return None

    return api_key
