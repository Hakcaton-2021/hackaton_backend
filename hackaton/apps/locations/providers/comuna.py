from typing import List, Optional, Union

from django.db.models.query import QuerySet

from hackaton.apps.locations.lib.exceptions.comuna import (
    CantCreateComuna,
    CantUpdateComunaStatus,
)
from hackaton.apps.locations.models import Comuna


def get_comuna_by_pk(pk: int) -> Optional[Comuna]:
    """
    Method to obtain comuna pk
    """
    try:
        comuna = Comuna.objects.get(pk=pk)
        return comuna
    except Comuna.DoesNotExist:
        return None


def get_comuna_by_country(country_pk: int, name: str) -> Optional[Comuna]:
    """
    Method to obtain a commune by country
    -Returns: Optional[Comuna]
    """
    try:
        comune = Comuna.objects.get(country__pk=country_pk, name=name)
        return comune
    except Comuna.DoesNotExist:
        return None


def get_all_comunas() -> Union[QuerySet, List[Comuna]]:
    """
    Method to get a list of all comunas
    -Returns: List[Comuna]
    """
    comunas = Comuna.objects.all().order_by("name")
    return comunas


def create_country(
    code: str,
    name: str,
    country: int,
) -> Optional[Comuna]:
    """
    Method to create an comuna
    -Returns: Optional[Comuna]
    """
    try:
        comuna = Comuna.objects.create(
            code=code,
            name=name,
            country=country,
        )
        comuna.save()
        return comuna
    except CantCreateComuna:
        return None


def get_active_comunas() -> Union[QuerySet, List[Comuna]]:
    """
    Method to obtain active comunas
    """
    comunas = Comuna.objects.filter(is_active=True).order_by("name")
    return comunas


def activate_comuna_by_pk(pk: int) -> Optional[Comuna]:
    """
    Method for activate comuna by pk
    - Returns: Comuna
    """
    try:
        comuna = get_comuna_by_pk(pk=pk)
        if not comuna:
            return None
        comuna.is_active = True
        comuna.save(update_fields=["is_active", "updated_at"])
        return comuna
    except CantUpdateComunaStatus:
        return None


def deactivate_comuna_by_pk(pk: int) -> Optional[Comuna]:
    """
    Method for deactivate comuna by pk
    - Returns: Comuna
    """
    try:
        comuna = get_comuna_by_pk(pk=pk)
        if not comuna:
            return None
        comuna.is_active = False
        comuna.save(update_fields=["is_active", "updated_at"])
        return comuna
    except CantUpdateComunaStatus:
        return None
