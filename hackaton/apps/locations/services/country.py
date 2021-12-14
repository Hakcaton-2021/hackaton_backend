from typing import List, Optional
from hackaton.apps.locations.providers import country as country_providers

def get_country_by_pk(pk: int) -> Optional["locations.Country"]:
    return country_providers.get_country_by_pk(pk=pk)

def get_country_by_name(name: str) -> Optional["locations.Country"]:
    return country_providers.get_country_by_name(name=name)

def get_all_countries() -> List["locations.Country"]:
    return country_providers.get_all_countries()

def create_country(code: str, name: str) -> Optional["locations.Country"]:
    return country_providers.create_country(code=code, name=name)

def get_active_country() -> List["locations.Country"]:
    return country_providers.get_active_country()

def activate_country_by_pk(pk: int) -> Optional["locations.Country"]:
    return country_providers.activate_country_by_pk(pk=pk)

def deactivate_country_by_pk(pk: int) -> Optional["locations.Country"]:
    return country_providers.deactivate_country_by_pk(pk=pk)