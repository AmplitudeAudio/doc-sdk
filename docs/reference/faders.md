---
title: Built-in Faders
description: Reference for the fade curves included with the Amplitude Audio SDK.
diataxis: reference
---

This reference documents the fader curves built into the Amplitude Audio SDK. Faders control how values transition over time for volume, gain, pitch, and other parameters.

## Overview

Amplitude includes eight built-in faders. All faders use a fast cubic Bézier curve evaluator with fixed endpoints at `(0, 0)` and `(1, 1)`.

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

The seven non-constant faders are cubic Béziers between `(0, 0)` and `(1, 1)`. The chart below plots each curve over `t ∈ [0, 1]`. The `Constant` fader is omitted because it is an instant step rather than a curve.

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "description": "Built-in Amplitude fader curves.",
  "width": "container",
  "height": 320,
  "data": { "url": "/static/data/fader-curves.json" },
  "mark": { "type": "line", "interpolate": "monotone", "strokeWidth": 2 },
  "encoding": {
    "x": { "field": "x", "type": "quantitative", "title": "t (input)", "scale": { "domain": [0, 1] } },
    "y": { "field": "y", "type": "quantitative", "title": "value", "scale": { "domain": [0, 1] } },
    "color": { "field": "fader", "type": "nominal", "title": "Fader" }
  }
}
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
      "id": 7678456242523,
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
instance->Set(0.0, 1.0, 1000.0); // from 0.0 to 1.0 over 1000 ms
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
- Review the [Fader API Reference](../api/class_sparky_studios_1_1_audio_1_1_amplitude_1_1_fader.md).
- Explore the [Buses Configuration Reference](../project/buses-config.md) for ducking setup.
