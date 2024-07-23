# Meteo.LT integration for Home Assistant
<img width="90" height="90" src="https://github.com/Brunas/meteo_lt/blob/main/images/icon.png?raw=true" style="float: left; margin-right: 20px; margin-top: 10px;" >

Home Assistant integration for Meteo.Lt REST API

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)
![Project Maintenance][maintenance-shield]

<a href="https://buymeacoffee.com/pdfdc52z8h" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 40px !important;width: 145px !important;" ></a>

This integration adds support for retrieving the Forecast data from [Api.Meteo.Lt](https://api.meteo.lt) and setting up following platforms in Home Assistant:

Platform | Description
-- | --
`weather` | A Home Assistant `weather` entity, with current data, and hourly forecast data. The first forecast record is treated as current data.
`sensor` | A Home Assistant `sensor` entity, with all available data taken from the forecast first record.

Minimum required version of Home Assistant is **2024.7.3** as this integration uses the new Weather entity forecast types and it does **not** create Forecast Attributes.

## Installation through HACS (Recommended Method)

This Integration is part of the default HACS store. Search for *Meteo.lt* under Integrations and install from there. After the installation of the files, you must restart Home Assistant, or else you will not be able to add WeatherFlow Forecast from the Integration Page.

If you are not familiar with HACS, or haven't installed it, I would recommend to [look through the HACS documentation](https://hacs.xyz/), before continuing. Even though you can install the Integration manually, I would recommend using HACS, as you would always be reminded when a new release is published.

## Manual Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
1. If you do not have a `custom_components` directory (folder) there, you need to create it.
1. In the `custom_components` directory (folder) create a new folder called `meteo_lt`.
1. Download _all_ the files from the `custom_components/meteo_lt/` directory (folder) in this repository.
1. Place the files you downloaded in the new directory (folder) you created.
1. Restart Home Assistant
1. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Meteo.Lt":
     - Enter latitude and longitude to use for the integration. Default values are Home Assistant Home location.
     - Unlimitted number of locations is supported - `weather.meteo_lt_ABCD` entity is created where `ABCD` is name of the nearest calculated place from available places in api.meteo.lt. Note, that if an entity for the same place exists, new entity gets numeric suffix to the name.

## Enable Debug Logging

If logs are needed for debugging or reporting an issue, use the following configuration.yaml:

```yaml
logger:
  default: error
  logs:
    custom_components.meteo_lt: debug
```

***

[commits-shield]: https://img.shields.io/github/commit-activity/y/Brunas/meteo_lt.svg?style=flat-square
[commits]: https://github.com/Brunas/meteo_lt/commits/main
[hacs]: https://github.com/hacs/integration
[hacsbadge]: https://img.shields.io/badge/HACS-Default-orange.svg?style=flat-square
[license-shield]: https://img.shields.io/github/license/Brunas/meteo_lt.svg?style=flat-square
[maintenance-shield]: https://img.shields.io/badge/maintainer-Brunas%20%40Brunas-blue.svg?style=flat-square
[releases-shield]: https://img.shields.io/github/release/Brunas/meteo_lt.svg?style=flat-square
[releases]: https://github.com/Brunas/meteo_lt/releases