from typing import List, Optional
from hackaton.apps.locations.providers import comuna as comuna_providers


def get_comuna_by_pk(pk: int) -> Optional["locations.Comuna"]:
    return comuna_providers.get_comuna_by_pk(pk=pk)


def get_comuna_by_name(name: str) -> Optional["locations.Comuna"]:
    return comuna_providers.get_comuna_by_name(name=name)


def get_comuna_by_country(country_pk: int, name: str) -> Optional["locations.Comuna"]:
    return comuna_providers.get_comuna_by_country(country_pk=country_pk, name=name)


def get_all_comunas() -> List["locations.Comuna"]:
    return comuna_providers.get_all_comunas()


def create_country(
    code: str,
    name: str,
    country: int,
) -> Optional["locations.Comuna"]:
    return comuna_providers.create_country(
        code=code,
        name=name,
        country=country,
    )


def get_active_comunas() -> List["locations.Comuna"]:
    return comuna_providers.get_active_comunas()


def activate_comuna_by_pk(pk: int) -> Optional["locations.Comuna"]:
    return comuna_providers.activate_comuna_by_pk(pk=pk)


def deactivate_comuna_by_pk(pk: int) -> Optional["locations.Comuna"]:
    return comuna_providers.deactivate_comuna_by_pk(pk=pk)
