from typing import List, Optional, Union

from django.db.models.query import QuerySet

from hackaton.apps.business.lib.exceptions.company import (
    CantCreateCompany,
    CantUpdateCompanyStatus,
)
from hackaton.apps.business.models import Company
from hackaton.apps.business.services import company

def get_company_by_pk(pk: int) -> Optional[Company]:
    """
    Method to obtain country ok
    """
    try:
        company = Company.objects.get(pk=pk)
        return company
    except Company.DoesNotExist:
        return None

def create_company(
    business_rut: str,
    business_name: str,
    business_giro: str,
    business_direction: str,
    business_phone: str,
    representative_name: str,
    representative_rut: str,
    representative_email: str,
    billing_rut: str,
    type: int,
    form: int,
    gratification: int,
    country: int,
    mutual: int,
    mutual_amount: float,
    parent: int,
    checking_account: int,
    checking_bank: int,
    payment_mobilization: int,
) -> Optional[Company]:
    """
    Method to create Company
    """
    try:
        company = Company.objects.create(
            business_rut=business_rut,
            business_name=business_name,
            business_giro=business_giro,
            business_direction=business_direction,
            business_phone=business_phone,
            representative_name=representative_name,
            representative_rut=representative_rut,
            representative_email=representative_email,
            billing_rut=billing_rut,
            type=type,
            form=form,
            gratification=gratification,
            country=country,
            mutual=mutual,
            mutual_amount=mutual_amount,
            parent=parent,
            checking_account=checking_account,
            checking_bank=checking_bank,
            payment_mobilization=payment_mobilization,
        )
        company.save()
        return company
    except CantCreateCompany:
        return None

def get_all_companies() -> Union[QuerySet, List[Company]]:
    """
    Method to obtain all companies
    - Returns: List[Company] 
    """
    companies = Company.objects.all()
    return companies