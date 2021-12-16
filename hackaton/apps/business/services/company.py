from typing import List, Optional, Union

from hackaton.apps.business.providers import company as company_providers

def get_company_by_pk(pk: int) -> Optional["business.Company"]:
    return company_providers.get_company_by_pk(pk=pk)

def create_compony(
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
) -> Optional["business.Company"]:
    return company_providers.create_company(
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

def get_all_companies() -> List["business.Company"]:
    return company_providers.get_all_companies()