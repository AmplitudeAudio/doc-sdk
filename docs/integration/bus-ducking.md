---
title: Bus Ducking
description: Configure automatic bus ducking to lower the volume of background audio when important sounds play.
diataxis: how-to
---

This guide explains how to configure **bus ducking** in Amplitude. Ducking automatically reduces the gain of one or more buses when a specific bus becomes active, ensuring that dialogue, voiceovers, or critical SFX remain audible over background music and ambience.

## Overview

Ducking is configured in the **buses file** (`*.buses.json`). When a bus with `duck_buses` entries starts playing a sound, the target buses are faded down. When the sound stops, the target buses fade back up.

## Basic Ducking Setup

Here's a simple example where the `voices` bus ducks the `music` and `ambience` buses. Each bus is defined as a top-level entry in the `buses` array; `child_buses` holds the IDs of child buses, and `duck_buses` entries reference target buses by their numeric `id`:

```json
{
  "buses": [
    {
      "id": 1,
      "name": "master",
      "gain": 1.0,
      "child_buses": [2, 3, 4]
    },
    {
      "id": 2,
      "name": "music",
      "gain": 1.0
    },
    {
      "id": 3,
      "name": "ambience",
      "gain": 1.0
    },
    {
      "id": 4,
      "name": "voices",
      "gain": 1.0,
      "duck_buses": [
        {
          "id": 2,
          "target_gain": 0.3,
          "fade_in": {
            "duration": 200,
            "fader": "EaseIn"
          },
          "fade_out": {
            "duration": 800,
            "fader": "EaseOut"
          }
        },
        {
          "id": 3,
          "target_gain": 0.5,
          "fade_in": {
            "duration": 100,
            "fader": "Linear"
          },
          "fade_out": {
            "duration": 1000,
            "fader": "Linear"
          }
        }
      ]
    }
  ]
}
```

## Ducking Parameters

| Parameter | Description |
|-----------|-------------|
| `id` | The numeric ID of the bus to duck. Must match an existing bus `id`. |
| `target_gain` | The gain level to fade down to (0.0 = silent, 1.0 = no change). |
| `fade_in.duration` | Duration in milliseconds to fade the target bus down when ducking starts. |
| `fade_in.fader` | The fader curve for the fade-in (duck-down) transition. |
| `fade_out.duration` | Duration in milliseconds to fade the target bus back up when ducking ends. |
| `fade_out.fader` | The fader curve for the fade-out (restore) transition. |

## Fader Curves

The fader curve controls how smoothly the ducking transition feels:

| Fader | Behavior | Best For |
|-------|----------|----------|
| `Linear` | Constant rate of change | Mechanical, subtle ducking |
| `EaseIn` | Slow start, fast end | Gentle fade-down |
| `EaseOut` | Fast start, slow end | Gentle restore |
| `EaseInOut` | Slow start and end | Smooth, natural transitions |
| `Exponential` | Exponential curve | Aggressive, punchy ducking |

## Hierarchical Ducking

Ducking works across the bus hierarchy. If a child bus is ducked, its parent bus continues to process normally, but the child bus and all its descendants receive reduced gain.

```
master (gain: 1.0)
├── music (gain: 1.0) ← ducks to 0.2 when voices play
│   ├── combat_music
│   └── exploration_music
├── sfx (gain: 1.0)
└── voices (gain: 1.0) ← triggers ducking on music
```

## Runtime Control

You can also trigger ducking manually at runtime:

```cpp
Bus voicesBus = amEngine->FindBus("voices");
Bus musicBus = amEngine->FindBus("music");

// Manually duck music when a cutscene starts
musicBus.SetGain(0.2f);

// Restore music when the cutscene ends
musicBus.SetGain(1.0f);
```

However, the declarative ducking system in the buses file is preferred because it automatically manages fade curves and handles overlapping sounds correctly.

## Multiple Ducking Sources

When multiple buses try to duck the same target, the most aggressive duck (lowest target gain) wins. When all ducking sources stop, the target bus fades back to its normal gain.

## Best Practices

- **Use asymmetric fade times**: Fast fade-in (50–200ms) and slow fade-out (500–1500ms) feel most natural.
- **Avoid extreme ducking**: Target gains below 0.1 can make background audio feel like it disappeared entirely.
- **Group related sounds**: Put all dialogue on one bus, all music on another, and all ambience on a third for clean ducking behavior.
- **Test with headphones**: Ducking behavior can feel different on speakers vs. headphones.

## Next Steps

- Review the [Buses Configuration Reference](../project/buses-config.md) for the full schema.
- Learn how to create [custom faders](../tutorials/custom-fader.md) for unique ducking curves.
