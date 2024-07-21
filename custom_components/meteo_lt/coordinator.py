"""coordinator.py"""

from datetime import timedelta
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .const import LOGGER, UPDATE_MINUTES


class MeteoLtCoordinator(DataUpdateCoordinator):
    """Class to manage fetching Meteo LT data."""

    def __init__(self, hass, api, nearest_place):
        """Initialize."""
        self.api = api
        self.nearest_place = nearest_place
        super().__init__(
            hass,
            LOGGER,
            name="Meteo LT",
            update_interval=timedelta(minutes=UPDATE_MINUTES),
        )

    async def _async_update_data(self):
        """Fetch data from API."""
        forecast = await self.api.get_forecast(self.nearest_place.code)
        LOGGER.debug("Forecast retrieved: %s", forecast)
        return forecast
