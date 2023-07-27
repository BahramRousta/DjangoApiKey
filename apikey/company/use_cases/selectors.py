from django.shortcuts import get_object_or_404
from apikey.company.models import Company


def get_company(company_id: int):
    return get_object_or_404(Company, id=company_id)