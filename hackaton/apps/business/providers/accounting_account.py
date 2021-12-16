from typing import List, Optional, Union

from django.db.models.query import QuerySet

from hackaton.apps.business.lib.exceptions.accounting_account import (
    CantCreateAccountingAccount,
)
from hackaton.apps.business.models import AccountingAccount

def get_accounting_account_by_pk(pk: int) -> Optional[AccountingAccount]:
    """
    Method to obtain accounting account pk
    - Returns: Optional[AccountingAccount]
    """
    try:
        accounting_account = AccountingAccount.objects.get(pk=pk)
        return accounting_account
    except AccountingAccount.DoesNotExist:
        return None

def create_accounting_account(
    company: int,
    name: str,
    code: str,
) -> Optional[AccountingAccount]:
    """
    Method to create accounting account
    - Returns: Optional[AccountingAccount]
    """
    try:
        accounting_account = AccountingAccount.objects.create(
            company=company,
            name=name,
            code=code,
        )
        accounting_account.save()
        return accounting_account
    except CantCreateAccountingAccount:
        return None

def get_all_accounting_account() -> Union[QuerySet, List[AccountingAccount]]:
    """
    Method to obtain all accounting account
    - Returns: List[AccountingAccount] 
    """
    accounting_account = AccountingAccount.objects.all()
    return accounting_account