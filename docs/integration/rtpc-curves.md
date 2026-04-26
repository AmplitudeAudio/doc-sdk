---
title: RTPC Curves in Practice
description: Learn how to map game parameters to audio properties using Real-Time Parameter Control curves.
diataxis: how-to
---

This guide explains how to use **RTPCs (Real-Time Parameter Controls)** with curves to dynamically adjust audio properties based on game state. RTPCs allow game values like player health, speed, or altitude to control gain, pitch, priority, and effect parameters in real time.

## Overview

An RTPC consists of:

1. **An RTPC asset** — Defines the parameter name, min/max range, and default value.
2. **A curve** — Maps the RTPC value to an audio property (gain, pitch, etc.).
3. **Runtime updates** — Your game code sets the RTPC value each frame.

## Creating an RTPC Asset

Define the RTPC in your project:

```json
{
  "id": 100,
  "name": "player_speed",
  "min_value": 0.0,
  "max_value": 20.0,
  "default_value": 0.0,
  "fade_settings": {
    "enabled": true,
    "fade_attack": {
      "duration": 50,
      "fader": "Linear"
    },
    "fade_release": {
      "duration": 200,
      "fader": "Linear"
    }
  }
}
```

| Parameter | Description |
|-----------|-------------|
| `min_value` | Minimum expected game value. |
| `max_value` | Maximum expected game value. |
| `default_value` | Value used before the game sets it. |
| `fade_settings` | Smooths abrupt value changes. `fade_attack` and `fade_release` are `FadeTransitionSettings` objects with `duration` (milliseconds) and `fader` fields. |

## Mapping Curves in Sound Assets

Reference the RTPC in a sound object and map it to a property using a curve:

```json
{
  "id": 10,
  "name": "engine_loop",
  "path": "sounds/engine.wav",
  "loop": { "enabled": true },
  "gain": {
    "rtpc": "player_speed",
    "curve": {
      "parts": [
        {
          "start": { "x": 0, "y": 0.2 },
          "end": { "x": 20, "y": 1.0 },
          "fader": "EaseIn"
        }
      ]
    }
  },
  "pitch": {
    "rtpc": "player_speed",
    "curve": {
      "parts": [
        {
          "start": { "x": 0, "y": 0.8 },
          "end": { "x": 20, "y": 1.5 },
          "fader": "Linear"
        }
      ]
    }
  }
}
```

In this example:

- **Gain** increases from 0.2 to 1.0 as speed goes from 0 to 20.
- **Pitch** increases from 0.8 to 1.5 as speed goes from 0 to 20.

## Curve Structure

Curves are defined by one or more **parts**, each with:

| Field | Description |
|-------|-------------|
| `start.x`, `start.y` | RTPC value and output value at the start of this part. |
| `end.x`, `end.y` | RTPC value and output value at the end of this part. |
| `fader` | The curve shape between start and end. |

### Multi-Part Curves

For non-linear mappings, use multiple parts:

```json
{
  "curve": {
    "parts": [
      {
        "start": { "x": 0, "y": 1.0 },
        "end": { "x": 50, "y": 0.8 },
        "fader": "Linear"
      },
      {
        "start": { "x": 50, "y": 0.8 },
        "end": { "x": 100, "y": 0.0 },
        "fader": "EaseIn"
      }
    ]
  }
}
```

This creates a piecewise curve: health drops slowly from 100 to 50, then rapidly from 50 to 0.

## Runtime Updates

Update the RTPC value from your game code each frame:

```cpp
// Get the RTPC handle
RtpcHandle playerSpeed = amEngine->GetRtpcHandle("player_speed");

// Set the value based on game state
playerSpeed->SetValue(player.GetCurrentSpeed());
```

The engine automatically applies the curve to all sound objects that reference this RTPC.

## Common Use Cases

### Engine RPM

Map vehicle speed to engine pitch and volume:

```cpp
rtpc->SetValue(vehicle.GetRPM());
```

### Health-Based Audio

Lower music volume and add a heartbeat effect as health decreases:

```cpp
rtpc->SetValue(player.GetHealthPercent());
```

### Altitude Wind

Increase wind volume and pitch as the player climbs:

```cpp
rtpc->SetValue(player.GetAltitude());
```

### Proximity Warning

Map distance to enemy as a warning tone pitch:

```cpp
rtpc->SetValue(nearestEnemy.GetDistance());
```

## Effect Parameter RTPCs

RTPCs can also control effect parameters. In the effect asset, use `rtpc` values:

```json
{
  "id": 20,
  "name": "lowpass_filter",
  "effect": "BiquadResonant",
  "parameters": [
    {
      "name": "frequency",
      "value": {
        "rtpc": "player_underwater_depth",
        "curve": {
          "parts": [
            {
              "start": { "x": 0, "y": 20000 },
              "end": { "x": 10, "y": 400 },
              "fader": "EaseIn"
            }
          ]
        }
      }
    }
  ]
}
```

As the player goes deeper underwater, the low-pass filter cutoff drops from 20kHz to 400Hz.

## Debugging RTPCs

Use the engine's logging to verify RTPC values:

```cpp
amLogInfo("Player speed RTPC: %.2f", playerSpeed->GetValue());
```

## Best Practices

- **Normalize RTPC ranges**: Define `min_value` and `max_value` to match your game's natural ranges.
- **Use fade settings**: Prevent audio artifacts from abrupt value changes.
- **Reuse RTPCs**: One RTPC can drive multiple properties (gain, pitch, priority, effect params).
- **Keep curves simple**: Start with single-part linear curves and add complexity only when needed.

## Next Steps

- Review the [RTPC Reference](../project/rtpc.md) for the full asset schema.
- Learn about [custom faders](../tutorials/custom-fader.md) to create unique curve shapes.
