from apikey.authentication.models import ApiKey
from apikey.company.interfaces import get_company_interface


def create_api_key(company_id: int):
    company = get_company_interface(company_id=company_id)
    return ApiKey.objects.create(company=company)