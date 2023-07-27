from apikey.company.models import Company


def create_company(company_name: str):
    return Company.objects.create(name=company_name)