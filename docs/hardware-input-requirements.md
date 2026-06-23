# Hardware Input Requirements

## Assumptions

- StegDJ consumes governed room, event, and listener-scope signals from StegEnviro, KnowledgeVault, or collective-environment-engine.
- StegDJ does not register hardware directly.
- Availability and part numbers must be refreshed before procurement.

## Done Definition

This file is done when every adaptive music request can declare which telemetry inputs influenced discovery, sequencing, or StegMusic handoff.

## Required Inputs By Function

| Function | Required input ids | Why needed | Candidate parts |
| --- | --- | --- | --- |
| Music response | `sound_level_features` | Detect whether playback is too quiet, too dominant, or appropriately supporting the room. | I2S MEMS sound sensor Product ID 3421; PDM option Product ID 4346. |
| Room energy | `presence_motion`, `distance_proximity` | Determine listener scope and event activity level. | SEN0395, Grove PIR family, VL53L1X Product ID 3967. |
| Atmosphere alignment | `ambient_light`, `temperature_humidity_pressure` | Coordinate music with lighting, comfort, and visual context. | BH1750 Product ID 4681; BME280 Product ID 2652. |
| Long-event fatigue context | `co2_air_quality` | Reduce intensity or repetition when comfort context suggests fatigue risk. | SCD-41 Product ID 5190. |

## Christmas Music Minimum

For `intent_christmas_music_example_001`, minimum required inputs are:

- host-declared target state
- `sound_level_features` as derived-only room signal
- `ambient_light` when coordinating with StegAtmos or StegVisual

Optional inputs:

- `presence_motion`
- `co2_air_quality`
- `temperature_humidity_pressure`

## Refusal Boundary

StegDJ must refuse adaptive music decisions when the target state is missing, data standing is missing, or the request requires identity-linked personalization without opt-in.
