# Meteo.LT by Brunas integration for Home Assistant
<img width="90" height="90" src="https://github.com/Brunas/meteo_lt_by_brunas/blob/main/images/icon.png?raw=true" style="float: left; margin-right: 20px; margin-top: 10px;" >

Home Assistant integration for Meteo.Lt REST API

>**NOTE:** Renamed since there will be/is official meteo.lt integration in Home Assistant core.


[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)
![Project Maintenance][maintenance-shield]
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

<a href="https://buymeacoffee.com/pdfdc52z8h" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="max-width: 30% !important;" ></a>

This integration adds support for retrieving the Forecast data from [Api.Meteo.Lt](https://api.meteo.lt) and setting up following platforms in Home Assistant:

| Platform  | Entity ID                                   | Description                                                                                                                           |
| --------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `weather` | `weather.meteo_lt_ABCD`                     | A Home Assistant `weather` entity, with current data, and hourly forecast data. The first forecast record is treated as current data. |
| `sensor`  | `sensor.meteo_lt_ABCD_current_conditions`   | Sensor with all available data taken from the forecast first record and native value set to `temperature`                             |
| `sensor`  | `sensor.meteo_lt_ABCD_temperature`          | Sensor with `temperature` attribute taken from the forecast first record                                                              |
| `sensor`  | `sensor.meteo_lt_ABCD_apparent_temperature` | Sensor with `apparent_temperature` attribute taken from the forecast first record                                                     |
| `sensor`  | `sensor.meteo_lt_ABCD_wind_speed`           | Sensor with `wind_speed` attribute taken from the forecast first record                                                               |
| `sensor`  | `sensor.meteo_lt_ABCD_wind_gust_speed`      | Sensor with `wind_gust_speed` attribute taken from the forecast first record                                                          |
| `sensor`  | `sensor.meteo_lt_ABCD_wind_bearing`         | Sensor with `wind_bearing` attribute taken from the forecast first record                                                             |
| `sensor`  | `sensor.meteo_lt_ABCD_cloud_coverage`       | Sensor with `cloud_coverage` attribute taken from the forecast first record                                                           |
| `sensor`  | `sensor.meteo_lt_ABCD_pressure`             | Sensor with `pressure` attribute taken from the forecast first record                                                                 |
| `sensor`  | `sensor.meteo_lt_ABCD_humidity`             | Sensor with `humidity` attribute taken from the forecast first record                                                                 |
| `sensor`  | `sensor.meteo_lt_ABCD_precipitation`        | Sensor with `precipitation` attribute taken from the forecast first record                                                            |
| `sensor`  | `sensor.meteo_lt_ABCD_condition`            | Sensor with `condition` attribute taken from the forecast first record                                                                |
| `sensor`  | `sensor.meteo_lt_ABCD_warnings`             | Sensor with `warnings` attribute taken from the forecast first record                                                                 |

Where `ABCD` is name of the nearest place calculated using place list downloaded from `api.meteo.lt`

Implementation has been done using Home Assistant version **2025.1.4**. Older versions could work too as long as the new Weather entity forecast types exist. Integration does **not** create Forecast Attributes.

>**NOTE:** At the moment of writing this - api.meteo.lt data renewal happens every 3 hours.

## Installation through HACS (Recommended Method)

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=Brunas&repository=meteo_lt_by_brunas&category=integration)

or

1. Go to HACS->Integrations
2. Add this repo into your HACS custom repositories
3. Search for `Meteo.Lt by Brunas Integration` and Download it
4. Restart your HomeAssistant
5. Go to Settings->Devices & Services
6. Shift reload your browser

### Setup the Integration

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=meteo_lt_by_brunas)

1. Click Add Integration
1. Search for `Meteo.Lt by Brunas`
1. Enter latitude and longitude to use for the integration. Default values are Home Assistant Home location.
1. Unlimitted number of locations is supported. If an entity for the same place exists, new entity gets numeric suffix to the name.
1. You're all set


## Manual Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
1. If you do not have a `custom_components` directory (folder) there, you need to create it.
1. In the `custom_components` directory (folder) create a new folder called `meteo_lt_by_brunas`.
1. Download _all_ the files from the `custom_components/meteo_lt_by_brunas/` directory (folder) in this repository.
1. Place the files you downloaded in the new directory (folder) you created.
1. Added `meteo_lt_by_brunas:` into your `configuration.yaml`
1. Restart Home Assistant
1. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for `Meteo.Lt by Brunas`:
     - Enter latitude and longitude to use for the integration. Default values are Home Assistant Home location.
     - Unlimitted number of locations is supported. If an entity for the same place exists, new entity gets numeric suffix to the name.

## Enable Debug Logging

If logs are needed for debugging or reporting an issue, turn debugging in integration UI or use the following configuration.yaml:

```yaml
logger:
  default: error
  logs:
    custom_components.meteo_lt_by_brunas: debug
```

## Inspired by

[WeatherFlow Cloud](https://www.home-assistant.io/integrations/weatherflow_cloud/)

[SMHI](https://www.home-assistant.io/integrations/smhi/)

[OpenWeatherMap](https://www.home-assistant.io/integrations/openweathermap/)


***

[commits-shield]: https://img.shields.io/github/commit-activity/y/Brunas/meteo_lt.svg?style=flat-square
[commits]: https://github.com/Brunas/meteo_lt_by_brunas/commits/main
[hacs]: https://github.com/hacs/integration
[hacsbadge]: https://img.shields.io/badge/HACS-Default-orange.svg?style=flat-square
[license-shield]: https://img.shields.io/github/license/Brunas/meteo_lt_by_brunas.svg?style=flat-square
[maintenance-shield]: https://img.shields.io/badge/maintainer-Brunas%20%40Brunas-blue.svg?style=flat-square
[releases-shield]: https://img.shields.io/github/release/Brunas/meteo_lt_by_brunas.svg?style=flat-square
[releases]: https://github.com/Brunas/meteo_lt_by_brunas/releases
