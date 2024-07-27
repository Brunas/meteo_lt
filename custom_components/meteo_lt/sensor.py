"""sensor.py"""

from functools import property
from typing import Any
from homeassistant.components.sensor import SensorEntity
from homeassistant.const import (
    UnitOfSpeed,
    UnitOfTemperature,
    UnitOfPressure,
    UnitOfPrecipitationDepth,
)
from homeassistant.core import callback
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN, LOGGER


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up Meteo.Lt sensor based on a config entry."""
    LOGGER.debug(
        "Sensor setting up input: hass.data - %s, config entry - %s",
        hass.data[DOMAIN][entry.entry_id],
        entry,
    )
    async_add_entities(
        [
            MeteoLtCurrentConditionsSensor(
                hass.data[DOMAIN][entry.entry_id]["coordinator"],
                hass.data[DOMAIN][entry.entry_id]["nearest_place"],
                entry,
            )
        ]
    )


class MeteoLtCurrentConditionsSensor(CoordinatorEntity, SensorEntity):
    """Representation of a Meteo.Lt Current Conditions Sensor."""

    def __init__(self, coordinator, nearest_place, config_entry):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._attr_name = (
            f"{config_entry.title} {nearest_place.name} - Current Conditions"
        )
        self._attr_unique_id = f"{config_entry.entry_id}-sensor"
        self._state = None

    @property
    def native_value(self):
        """Return the value of the sensor."""
        return self.coordinator.data.current_conditions().temperature

    @property
    def extra_state_attributes(self) -> dict[str, Any] | None:
        """Return the state attributes."""
        current_conditions = self.coordinator.data.current_conditions()
        LOGGER.debug("Current conditions: %s", current_conditions)

        return {
            "native_temperature": current_conditions.temperature,
            "native_apparent_temperature": current_conditions.apparent_temperature,
            "native_wind_speed": current_conditions.wind_speed,
            "native_wind_gust_speed": current_conditions.wind_gust_speed,
            "wind_bearing": current_conditions.wind_bearing,
            "cloud_coverage": current_conditions.cloud_coverage,
            "native_pressure": current_conditions.pressure,
            "humidity": current_conditions.humidity,
            "native_precipitation": current_conditions.precipitation,
            "condition": current_conditions.condition,
            "native_temperature_unit": UnitOfTemperature.CELSIUS,
            "native_wind_speed_unit": UnitOfSpeed.METERS_PER_SECOND,
            "native_pressure_unit": UnitOfPressure.HPA,
            "native_precipitation_unit": UnitOfPrecipitationDepth.MILLIMETERS,
        }

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        LOGGER.debug(f"Handling Meteo.Lt sensor coordinator update for entity {self.entity_id}")
        self.async_write_ha_state()

    async def async_update(self):
        """Fetch new state data for the sensor."""
        LOGGER.debug(f"Updating Meteo.Lt sensor entity {self.entity_id}")
        await self.coordinator.async_request_refresh()
