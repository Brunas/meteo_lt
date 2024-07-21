"""__init__.py"""

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

from meteo_lt import MeteoLtAPI
from .const import DOMAIN, LOGGER
from .coordinator import MeteoLtCoordinator

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Meteo LT component."""
    LOGGER.info("Setting up Meteo LT")
    hass.data.setdefault(DOMAIN, {})
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Meteo LT from a config entry."""
    LOGGER.info("Setting up Meteo LT from config entry")

    api = MeteoLtAPI()
    latitude = entry.data.get("latitude", hass.config.latitude)
    longitude = entry.data.get("longitude", hass.config.longitude)
    LOGGER.debug("Configured coordinates: %s, %s", latitude, longitude)

    nearest_place = await api.get_nearest_place(latitude, longitude)
    LOGGER.debug("Nearest place found: %s", nearest_place)

    coordinator = MeteoLtCoordinator(hass, api, nearest_place)
    await coordinator.async_refresh()

    hass.data[DOMAIN][entry.entry_id] = {
        "api": api,
        "nearest_place": nearest_place,
        "coordinator": coordinator,
    }

    await hass.config_entries.async_forward_entry_setups(entry, ["weather"])

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    LOGGER.info("Unloading Meteo LT config entry")

    unload_ok = await hass.config_entries.async_forward_entry_unload(entry, "weather")
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok
