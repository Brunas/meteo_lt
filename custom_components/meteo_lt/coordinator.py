"""coordinator.py"""

from datetime import datetime, timedelta, timezone
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.util import dt

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

    def _is_daytime(self, forecast_time_utc):
        """Check if it's daytime using sun sensor data."""
        sun_state = self.hass.states.get("sun.sun")
        if not sun_state:
            return True

        next_rising_utc = dt.parse_datetime(sun_state.attributes["next_rising"])
        next_setting_utc = dt.parse_datetime(sun_state.attributes["next_setting"])

        return next_rising_utc <= forecast_time_utc <= next_setting_utc

    def _map_condition(self, condition_code, forecast_time_utc):
        """Map API weather condition to HA condition."""
        is_day = self._is_daytime(forecast_time_utc)
        condition_mapping = {
            "clear": "sunny" if is_day else "clear-night",
            "partly-cloudy": "partlycloudy",
            "cloudy-with-sunny-intervals": "partlycloudy",
            "cloudy": "cloudy",
            "thunder": "lightning",
            "isolated-thunderstorms": "lightning-rainy",
            "thunderstorms": "lightning-rainy",
            "heavy-rain-with-thunderstorms": "lightning-rainy",
            "light-rain": "rainy",
            "rain": "rainy",
            "heavy-rain": "pouring",
            "light-sleet": "snowy-rainy",
            "sleet": "snowy-rainy",
            "freezing-rain": "snowy-rainy",
            "hail": "hail",
            "light-snow": "snowy",
            "snow": "snowy",
            "heavy-snow": "snowy",
            "fog": "fog",
            None: "exceptional",
        }
        return condition_mapping.get(condition_code, "exceptional")

    async def _async_update_data(self):
        """Fetch data from API."""
        forecast_data = await self.api.get_forecast(self.nearest_place.code)

        for forecast in forecast_data:
            forecast_time_utc = dt.parse_datetime(forecast["datetime"])
            if "condition_code" in forecast:
                forecast["condition"] = self._map_condition(
                    forecast["condition_code"], forecast_time_utc
                )

        LOGGER.debug("Forecast calculated: %s", forecast_data)

        self.last_updated = datetime.now().astimezone(timezone.utc).isoformat()
        return forecast_data
