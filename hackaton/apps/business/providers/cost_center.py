from typing import List, Optional, Union

from django.db.models.query import QuerySet

from hackaton.apps.business.lib.exceptions.cost_center import (
    CantCreateCost_Center,
    CantUpdateCost_CenterStatus,
)
from hackaton.apps.business.models import CostCenter

def get_cost_center_by_pk(pk: int) -> Optional[CostCenter]:
    """
    Method to obtain country ok
    """
    try:
        cost_center = CostCenter.objects.get(pk=pk)
        return cost_center
    except CostCenter.DoesNotExist:
        return None

def create_cost_center(
    company: int,
    name: str,
    code: str,
    parent: int,
) -> Optional[CostCenter]:
    """
    Method to create cost center
    - Returns: Optional[CostCenter]
    """
    try:
        cost_center = CostCenter.objects.create(
            company=company,
            name=name,
            code=code,
            parent=parent,
        )
        cost_center.save()
        return cost_center
    except CantCreateCost_Center:
        return None

def get_all_cost_center() -> Union[QuerySet, List[CostCenter]]:
    """
    Method to obtain all cost center
    - Returns: List[CostCenter] 
    """
    cost_center = CostCenter.objects.all()
    return cost_center