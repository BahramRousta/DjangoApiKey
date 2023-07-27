from apikey.company.use_cases.selectors import get_company


def get_company_interface(company_id: int):
    return get_company(company_id=company_id)