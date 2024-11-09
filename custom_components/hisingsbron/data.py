"""Custom types for hisingsbron."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import HisingsbronApiClient
    from .coordinator import BlueprintDataUpdateCoordinator


type HisingsbronConfigEntry = ConfigEntry[HisingsbronData]


@dataclass
class HisingsbronData:
    """Data for the Blueprint integration."""

    client: HisingsbronApiClient
    coordinator: BlueprintDataUpdateCoordinator
    integration: Integration
