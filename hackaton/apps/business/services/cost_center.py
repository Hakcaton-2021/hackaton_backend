from typing import List, Optional, Union

from hackaton.apps.business.providers import cost_center as cost_center_providers

def get_cost_center_by_pk(pk: int) -> Optional["business.CostCenter"]:
    return cost_center_providers.get_cost_center_by_pk(pk=pk)

def create_cost_center(
    company: int,
    name: str,
    code: str,
    parent: int,
) -> Optional["business.CostCenter"]:
    return cost_center_providers.create_cost_center(
        company=company,
        name=name,
        code=code,
        parent=parent,
    )

def get_all_cost_center() -> List["business.CostCenter"]:
    return cost_center_providers.get_all_cost_center()