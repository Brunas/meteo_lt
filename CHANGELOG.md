## Release 0.4.0

Date: `2025-10-04`

### Changes

- Upped `meteo_lt-pkg` version to support weather warnings which will require more work to make them nicely available in Home Assistant
- Upped `homeassistant` package version to `2025.1.4`

## Release 0.3.1

Date: `2025-09-30`

### Changes

- HA helper function `sun.is_up` used to identify day

## Release 0.3.0

Date: `2025-09-29`

### Changes

- Introduction condition map from meteo.lt API to HASS (moved from `meteo_lt-pkg`)
- Fixed night time clear sky condition using `sun.sun` state value `above_horizon`
- Usual version bumps

## Release 0.2.6

Date: `2025-05-10`

### Changes

- `Forecast` object usage
- `async_added_to_hass` callback for sensors/weather entity
- Readme and changelog document update
- Usual version bumps

## Release 0.2.5

Date: `2025-03-08`

### Changes

- Country in `hacs.json`
- Usual version bumps

## Release 0.2.4

Date: `2025-01-14`

### Changes

- Daily `dependabot`
- `meteo_lt-pkg` specific version in `requirements.txt`
- Usual version bumps

## Release 0.2.3

Date: `2024-07-31`

### Changes

- Dependabot bumps
- Tweaked sensor device and state classes and units of measurement

## Release 0.2.2

Date: `2024-07-28`

### Changes

- Bumped meteo_lt-pkg to 0.2.2
- Removing of past hours forecasts
- Current conditions is the current hour record
- Forecast creation time stamp in attributes

## Release 0.2.1

Date: `2024-07-28`

### Changes

- Bumped meteo_lt-pkg to 0.2.1 to change UTC datetime format from "Z" to "+00:00"
- Devcontainer fixes and improvements
- Readme update

## Release 0.2.0

Date: `2024-07-27`

### Changes

- Separate sensors for every current conditions attribute
- Added last_updated to all entities to see coordinator working
- Trying to fix updating

## Release 0.1.8

Date: `2024-07-26`

### Changes

- Bumped meteo_lt-pkg to 0.2.0

## Release 0.1.7

Date: `2024-07-25`

### Changes

- Bumped meteo_lt-pkg to 0.1.6

## Release 0.1.6

Date: `2024-07-25`

### Changes

- Readme tweaking

## Not a Release 0.1.x

Date: `2024-07-24`

### Changes

- Initial version moved from local HASS