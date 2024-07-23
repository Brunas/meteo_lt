"""weather.py"""

# pylint: disable=unused-argument, abstract-method

from functools import cached_property
from typing import List, Dict, Union
from homeassistant.components.weather import WeatherEntity, WeatherEntityFeature
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    UnitOfSpeed,
    UnitOfTemperature,
    UnitOfPressure,
    UnitOfPrecipitationDepth,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType, DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN, LOGGER


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    """Set up Meteo.Lt weather based on a config entry."""
    LOGGER.debug("Weather Setting up config entry %s", entry)
    coordinator = hass.data[DOMAIN][entry.entry_id]["coordinator"]
    nearest_place = hass.data[DOMAIN][entry.entry_id]["nearest_place"]
    async_add_entities([MeteoLtWeather(coordinator, nearest_place, entry)], True)


class MeteoLtWeather(CoordinatorEntity, WeatherEntity):
    """Meteo.lt WeatherEntity implementation"""

    def __init__(self, coordinator, nearest_place, config_entry):
        """__init__"""
        super().__init__(coordinator)
        self._name = f"Meteo.Lt {nearest_place.name}"
        self._attr_unique_id = config_entry.entry_id

    @property
    def name(self):
        """Name"""
        return self._name

    @property
    def device_info(self):
        """device info"""
        return {
            "entry_type": DeviceEntryType.SERVICE,
            "identifiers": {(DOMAIN, self._attr_unique_id)},
            "name": self._name,
            "manufacturer": "Meteo.Lt"
        }

    @cached_property
    def native_temperature(self):
        """Native temperature"""
        return self.coordinator.data.forecast_timestamps[0].temperature

    @cached_property
    def native_temperature_unit(self):
        """Native temperature unit"""
        return UnitOfTemperature.CELSIUS

    @cached_property
    def humidity(self):
        """Humidity"""
        return self.coordinator.data.forecast_timestamps[0].humidity

    @cached_property
    def native_wind_speed(self):
        """Native wind speed"""
        return self.coordinator.data.forecast_timestamps[0].wind_speed

    @cached_property
    def native_wind_speed_unit(self):
        """Native wind speed unit"""
        return UnitOfSpeed.METERS_PER_SECOND

    @cached_property
    def wind_bearing(self):
        """Native wind bearing"""
        return self.coordinator.data.forecast_timestamps[0].wind_bearing

    @cached_property
    def native_pressure(self):
        """Native pressure"""
        return self.coordinator.data.forecast_timestamps[0].pressure

    @cached_property
    def native_pressure_unit(self):
        """Native pressure unit"""
        return UnitOfPressure.HPA

    @cached_property
    def native_precipitation(self):
        """Native precipitation"""
        return self.coordinator.data.forecast_timestamps[0].precipitation

    @cached_property
    def native_precipitation_unit(self):
        """Native precipitation unit"""
        return UnitOfPrecipitationDepth.MILLIMETERS

    @cached_property
    def condition(self):
        """Condition"""
        return self.coordinator.data.forecast_timestamps[0].condition

    @cached_property
    def cloud_coverage(self):
        """Cloud coverage"""
        return self.coordinator.data.forecast_timestamps[0].cloud_coverage

    @cached_property
    def native_apparent_temperature(self):
        """Native apparent temperature"""
        return self.coordinator.data.forecast_timestamps[0].apparent_temperature

    @cached_property
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
                "native_temperature_unit": UnitOfTemperature.CELSIUS,
                "native_wind_speed_unit":UnitOfSpeed.METERS_PER_SECOND,
                "native_pressure_unit": UnitOfPressure.HPA,
                "native_precipitation_unit": UnitOfPrecipitationDepth.MILLIMETERS,
            }
            for entry in self.coordinator.data.forecast_timestamps
        ]
        LOGGER.debug("Hourly_forecast created: %s", hourly_forecast)
        return hourly_forecast

    async def async_update(self):
        """Refreshing coordinator"""
        LOGGER.debug("Updating MeteoLtWeather entity.")
        await self.coordinator.async_request_refresh()
