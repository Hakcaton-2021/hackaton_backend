from typing import List, Optional, Union

from hackaton.apps.business.providers import accounting_account as accounting_account_providers

def get_accounting_account_by_pk(pk: int) -> Optional["business.AccountingAccount"]:
    return accounting_account_providers.get_accounting_account_by_pk(pk=pk)

def create_accounting_account(
    company: int,
    name: str,
    code: str,
) -> Optional["business.AccountingAccount"]:
    return accounting_account_providers.create_accounting_account(
        company=company,
        name=name,
        code=code,
    )

def get_all_accounting_account() -> List["business.AccountingAccount"]:
    return accounting_account_providers.get_all_accounting_account()