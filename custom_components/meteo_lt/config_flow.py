"""config_flow.py"""

# pylint: disable=too-few-public-methods

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import HomeAssistant

from .const import DOMAIN


class MeteoLtConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Meteo LT."""
    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            # Handle the user input and validation here
            return self.async_create_entry(title="Meteo.Lt", data=user_input)

        # Get the default values from Home Assistant configuration
        hass_config = self.hass.config
        default_latitude = hass_config.latitude
        default_longitude = hass_config.longitude

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("latitude", default=default_latitude): float,
                vol.Required("longitude", default=default_longitude): float,
            })
        )