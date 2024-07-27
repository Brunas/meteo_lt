"""coordinator.py"""

from datetime import datetime, timedelta
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .const import MANUFACTURER, LOGGER, UPDATE_MINUTES


class MeteoLtCoordinator(DataUpdateCoordinator):
    """Class to manage fetching Meteo LT data."""

    def __init__(self, hass, api, nearest_place):
        """Initialize."""
        self.api = api
        self.nearest_place = nearest_place
        self.last_updated = None
        super().__init__(
            hass,
            LOGGER,
            name=MANUFACTURER,
            update_interval=timedelta(minutes=UPDATE_MINUTES),
            always_update=True,
        )

    async def _async_update_data(self):
        """Fetch data from API."""
        forecast = await self.api.get_forecast(self.nearest_place.code)
        LOGGER.debug("Forecast retrieved: %s", forecast)
        self.last_updated = datetime.now().isoformat()
        return forecast
