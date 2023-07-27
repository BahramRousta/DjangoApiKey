from apikey.authentication.models import ApiKey


def get_api_key(api_key):
    return ApiKey.objects.filter(api_key=api_key).exists()