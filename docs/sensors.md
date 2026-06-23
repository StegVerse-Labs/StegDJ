# Sensors

## Assumptions

- StegDJ does not own raw sensors. It consumes authorized listener, room, event, and music-response signals from StegEnviro, KnowledgeVault, or collective-environment-engine.
- Product availability is a dated procurement snapshot and must be refreshed before purchase.
- Music adaptation must not infer or choose a target state silently. The target state must be declared by the listener, host, event profile, or another authorized path.

## Done Definition

This section is done when StegDJ can explain which sensor-derived signals influence discovery, playback, sequencing, and StegMusic requests.

## How Sensors Are Used Here

StegDJ uses sensor-derived state to choose music, sequence tracks, adjust energy, or request new music from StegMusic.

Example uses:

- sound-level trends indicate whether the room is too quiet, too loud, or socially active;
- conversation density can inform whether music should recede, warm the room, or increase energy;
- ambient light and atmosphere state can coordinate music with visual and lighting profiles;
- temperature, humidity, and CO2 can contribute to comfort-aware music pacing;
- occupancy and motion can determine whether playback should target one listener, a room, or an event.

## Candidate Sensor Inputs

| Sensor class | Use in StegDJ | Candidate parts / vendors | Availability snapshot |
| --- | --- | --- | --- |
| Sound-level feature extraction | Noise contour, conversation density, music response | Adafruit I2S MEMS Microphone SPH0645LM4H, Product ID 3421; Adafruit PDM Microphone, Product ID 4346 | Adafruit listed product 3421 in stock at snapshot time; product 4346 exists as a PDM option. |
| Ambient light | Coordinate music energy with lighting and visuals | Adafruit BH1750, Product ID 4681 | Adafruit listed product 4681 in stock at snapshot time. |
| Temperature / humidity / pressure | Comfort-aware pacing and atmosphere coordination | Adafruit BME280, Product ID 2652 | Adafruit listed product 2652 in stock at snapshot time. |
| CO2 / air quality | Fatigue and ventilation context for long events | Adafruit SCD-41, Product ID 5190 | Adafruit listed product 5190 with stock at snapshot time. |
| Presence / motion | Determine listener scope and event-room activity level | DFRobot SEN0395 mmWave; Grove PIR motion modules; VL53L1X zones | Refresh vendor availability before procurement. |

## Music Boundary

StegDJ should prefer aggregate or derived state. Raw sound must not be retained or transcribed by default. Identity-linked personalization requires explicit opt-in through the broader StegVerse governance path.

## Next Build Step

Add `schemas/music-sensor-context.schema.json` and an example that maps room-state signals into a music selection request.
