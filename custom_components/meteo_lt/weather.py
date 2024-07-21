"""weather.py"""

# pylint: disable=unused-argument, abstract-method

from typing import List, Dict, Union
from homeassistant.components.weather import WeatherEntity, WeatherEntityFeature
from homeassistant.const import (
    UnitOfSpeed,
    UnitOfTemperature,
    UnitOfPressure,
    UnitOfPrecipitationDepth,
)
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN, LOGGER


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Setting up platform"""
    LOGGER.debug("Setting up platform")
    coordinator = hass.data[DOMAIN]["coordinator"]
    nearest_place = hass.data[DOMAIN]["nearest_place"]
    async_add_entities([MeteoLtWeather(coordinator, nearest_place)], True)


class MeteoLtWeather(CoordinatorEntity, WeatherEntity):
    """Meteo.lt WeatherEntity implementation"""

    def __init__(self, coordinator, nearest_place):
        """__init__"""
        super().__init__(coordinator)
        self._name = f"Meteo LT {nearest_place.name}"

    @property
    def name(self):
        """Name"""
        return self._name

    @property
    def native_temperature(self):
        """Native temperature"""
        return self.coordinator.data.forecast_timestamps[0].temperature

    @property
    def native_temperature_unit(self):
        """Native temperature unit"""
        return UnitOfTemperature.CELSIUS

    @property
    def humidity(self):
        """Humidity"""
        return self.coordinator.data.forecast_timestamps[0].humidity

    @property
    def native_wind_speed(self):
        """Native wind speed"""
        return self.coordinator.data.forecast_timestamps[0].wind_speed

    @property
    def native_wind_speed_unit(self):
        """Native wind speed unit"""
        return UnitOfSpeed.METERS_PER_SECOND

    @property
    def wind_bearing(self):
        """Native wind bearing"""
        return self.coordinator.data.forecast_timestamps[0].wind_bearing

    @property
    def native_pressure(self):
        """Native pressure"""
        return self.coordinator.data.forecast_timestamps[0].pressure

    @property
    def native_pressure_unit(self):
        """Native pressure unit"""
        return UnitOfPressure.HPA

    @property
    def native_precipitation(self):
        """Native precipitation"""
        return self.coordinator.data.forecast_timestamps[0].precipitation

    @property
    def native_precipitation_unit(self):
        """Native precipitation unit"""
        return UnitOfPrecipitationDepth.MILLIMETERS

    @property
    def condition(self):
        """Condition"""
        return self.coordinator.data.forecast_timestamps[0].condition

    @property
    def cloud_coverage(self):
        """Cloud coverage"""
        return self.coordinator.data.forecast_timestamps[0].cloud_coverage

    @property
    def native_apparent_temperature(self):
        """Native apparent temperature"""
        return self.coordinator.data.forecast_timestamps[0].apparent_temperature

    @property
    def native_wind_gust_speed(self):
        """Native wind gust speed"""
        return self.coordinator.data.forecast_timestamps[0].wind_gust_speed

    @property
    def supported_features(self):
        """Return the list of supported features."""
        return WeatherEntityFeature.FORECAST_HOURLY

    async def async_forecast_hourly(
        self,
    ) -> Union[List[Dict[str, Union[str, float]]], None]:
        """Return the hourly forecast in native units."""
        if not self.supported_features & WeatherEntityFeature.FORECAST_HOURLY:
            return None

        hourly_forecast = [
            {
                "datetime": entry.datetime,
                "native_temperature": entry.temperature,
                "native_apparent_temperature": entry.apparent_temperature,
                "native_wind_speed": entry.wind_speed,
                "native_wind_gust_speed": entry.wind_gust_speed,
                "wind_bearing": entry.wind_bearing,
                "cloud_coverage": entry.cloud_coverage,
                "native_pressure": entry.pressure,
                "humidity": entry.humidity,
                "native_precipitation": entry.precipitation,
                "condition": entry.condition,
            }
            for entry in self.coordinator.data.forecast_timestamps
        ]
        LOGGER.debug("Hourly_forecast created: %s", hourly_forecast)
        return hourly_forecast

    async def async_update(self):
        """Refreshing coordinator"""
        LOGGER.debug("Updating MeteoLtWeather entity.")
        await self.coordinator.async_request_refresh()
