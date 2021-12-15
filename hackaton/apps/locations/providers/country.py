from typing import List, Optional, Union

from django.db.models.query import QuerySet

from hackaton.apps.locations.lib.exceptions.country import (
    CantCreateCountry,
    CantUpdateCountryStatus,
)
from hackaton.apps.locations.models import Country


def get_country_by_pk(pk: int) -> Optional[Country]:
    """
    Method to obtain country ok
    """
    try:
        country = Country.objects.get(pk=pk)
        return country
    except Country.DoesNotExist:
        return None


def get_country_by_name(name: str) -> Optional[Country]:
    """
    Method to obtain a country by name
    """
    try:
        country = Country.objects.get(name=name)
        return country
    except Country.DoesNotExist:
        return None


def get_all_countries() -> Union[QuerySet, List[Country]]:
    """
    Method to get a list of all countries
    -Returns: List[Country]
    """
    countries = Country.objects.all().order_by("name")
    return countries


def create_country(
    code: str,
    name: str,
) -> Optional[Country]:
    """
    Method to create an country
    -Returns: Optional[Country]
    """
    try:
        country = Country.objects.create(code=code, name=name)
        country.save()
        return country
    except CantCreateCountry:
        return None


def get_active_country() -> Union[QuerySet, List[Country]]:
    """
    Method to obtain active country
    """
    country = Country.objects.filter(is_active=True).order_by("name")
    return country


def activate_country_by_pk(pk: int) -> Optional[Country]:
    """
    Method for activate country by pk
    - Returns: Country
    """
    try:
        country = get_country_by_pk(pk=pk)
        if not country:
            return None
        country.is_active = True
        country.save(update_fields=["is_active", "updated_at"])
        return country
    except CantUpdateCountryStatus:
        return None


def deactivate_country_by_pk(pk: int) -> Optional[Country]:
    """
    Method for deactivate country by pk
    - Returns: Country
    """
    try:
        country = get_country_by_pk(pk=pk)
        if not country:
            return None
        country.is_active = False
        country.save(update_fields=["is_active", "updated_at"])
        return country
    except CantUpdateCountryStatus:
        return None
