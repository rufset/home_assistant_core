"""Hello State integration."""

from __future__ import annotations

import voluptuous as vol

from homeassistant.core import HomeAssistant
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.typing import ConfigType

DOMAIN = "hello_state"


# No configuration options → empty schema
CONFIG_SCHEMA = vol.Schema(
    {DOMAIN: cv.empty_config_schema(DOMAIN)}, extra=vol.ALLOW_EXTRA
)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Hello State integration."""
    hass.states.async_set(f"{DOMAIN}.world", "Hello, state!")
    return True
