---
title: Built-in Faders
description: Reference for the fade curves included with the Amplitude Audio SDK.
---

This reference documents the fader curves built into the Amplitude Audio SDK. Faders control how values transition over time for volume, gain, pitch, and other parameters.

## Overview

Amplitude includes nine built-in faders. All faders use a fast cubic Bézier curve evaluator with fixed endpoints at `(0, 0)` and `(1, 1)`.

| Fader | Control Points `(x1, y1, x2, y2)` | Behavior |
|-------|-----------------------------------|----------|
| **Constant** | `(0, 0, 0, 0)` | Instant change; no transition. |
| **Linear** | `(0, 0, 1, 1)` | Constant rate of change. |
| **Ease** | `(0.25, 0.1, 0.25, 1.0)` | Smooth start and end (CSS default). |
| **EaseIn** | `(0.42, 0, 1.0, 1.0)` | Slow start, fast end. |
| **EaseOut** | `(0, 0, 0.58, 1.0)` | Fast start, slow end. |
| **EaseInOut** | `(0.42, 0, 0.58, 1.0)` | Slow start and end, fast middle. |
| **Exponential** | `(0.9, 0.05, 0.95, 0.95)` | Sharp exponential curve. |
| **SCurve** | `(0.4, 0.0, 0.6, 1.0)` | S-shaped sigmoid curve. |

## Curve Visualization

```
Constant    Linear      Ease        EaseIn      EaseOut     EaseInOut   Exponential SCurve
│           │           │           │           │           │           │           │
1●          │        ●●●│           │        ●●●│        ●●●│        ●●●│        ●●●│        ●●●
│           │      ●│   │         ●●│      ●│   │      ●│   │    ●●│   │    ●●●│   │    ●●│   │
│           │    ●│   │ │       ●│  │    ●│   │ │    ●│   │ │  ●│  │   │ │  ●│  │   │ │  ●│  │   │ │
│           │  ●│   │   │     ●│    │  ●│   │   │  ●│   │   │●│   │   │   │●│   │   │   │●│   │   │   │
│           │●│   │     │   ●│      │●│   │     │●│   │     ││   │     │   ││   │     │   ││   │     │   │
0●──────────●│   │       │ ●│        ●│   │       ●│   │       │   │       │   │   │       │   │   │       │   │
 0         1 0         1 0         1 0         1 0         1 0         1 0         1 0         1
```

## Usage in Assets

Faders are referenced by name in project assets:

### Sound Object Fader

```json
{
  "id": 10,
  "name": "explosion",
  "path": "sounds/explosion.wav",
  "fader": "EaseOut"
}
```

### Bus Ducking Fade

```json
{
  "duck_buses": [
    {
      "target_bus": "music",
      "target_gain": 0.3,
      "fade_in": {
        "duration": 200,
        "fader": "EaseIn"
      },
      "fade_out": {
        "duration": 800,
        "fader": "EaseOut"
      }
    }
  ]
}
```

### RTPC Curve

```json
{
  "curve": {
    "parts": [
      {
        "start": { "x": 0, "y": 0 },
        "end": { "x": 1, "y": 1 },
        "fader": "Linear"
      }
    ]
  }
}
```

## Runtime API

You can create fader instances programmatically:

```cpp
// Get a fader by name
auto fader = Fader::Find("EaseInOut");

// Create an instance
auto instance = fader->CreateInstance();

// Configure the transition
instance->Set(0.0, 1.0, 1000.0); // from 0.0 to 1.0 over 1000ms
instance->Start(0.0);

// Query the value at a given time
AmReal64 value = instance->GetFromTime(currentTime);
```

## When to Use Each Fader

| Scenario | Recommended Fader | Reason |
|----------|-------------------|--------|
| UI button clicks | `Constant` or `Linear` | Immediate or fast feedback |
| Music crossfades | `EaseInOut` | Smooth, natural transition |
| Bus ducking (fade down) | `EaseIn` | Gentle reduction |
| Bus ducking (restore) | `EaseOut` | Gentle return |
| Explosion impacts | `Exponential` | Aggressive, punchy |
| Ambient fade-ins | `SCurve` | Slow, imperceptible start |
| Cinematic transitions | `Ease` | Balanced, polished feel |

## Custom Faders

If the built-in curves do not meet your needs, you can implement a custom fader by subclassing `Fader` and `FaderInstance`. See the [Custom Fader Tutorial](../tutorials/custom-fader.md) for a step-by-step guide.

## Next Steps

- Learn how to create a [custom fader](../tutorials/custom-fader.md).
- Review the [Fader API Reference](../api/engine/Fader.md).
- Explore the [Buses Configuration Reference](../project/buses-config.md) for ducking setup.
