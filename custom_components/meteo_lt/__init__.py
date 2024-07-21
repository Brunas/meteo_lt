"""__init__.py"""

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from homeassistant.helpers.discovery import async_load_platform

from meteo_lt import MeteoLtAPI

from .const import DOMAIN, LOGGER
from .coordinator import MeteoLtCoordinator


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Meteo LT component."""
    LOGGER.info("Setting up Meteo LT")

    api = MeteoLtAPI()
    latitude = hass.config.latitude
    longitude = hass.config.longitude
    LOGGER.debug("HASS Home coordinates: %s, %s", latitude, longitude)

    # Retrieve the nearest place once during setup
    nearest_place = await api.get_nearest_place(latitude, longitude)
    LOGGER.debug("Nearest place found: %s", nearest_place)

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN]["api"] = api
    hass.data[DOMAIN]["nearest_place"] = nearest_place

    coordinator = MeteoLtCoordinator(hass, api, nearest_place)
    await coordinator.async_refresh()

    hass.data[DOMAIN]["coordinator"] = coordinator

    hass.async_create_task(async_load_platform(hass, "weather", DOMAIN, {}, config))

    return True
