"""config_flow.py"""

from typing import Any

from homeassistant import config_entries

from .const import DOMAIN


class MeteoLtConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Meteo LT."""

    VERSION = 1

    async def async_step_user(self, user_input: dict[str, Any] = None):
        """Handle the initial step."""
        return self.async_create_entry(title="Meteo LT", data={})
