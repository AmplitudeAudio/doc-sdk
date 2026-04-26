---
title: Multi-Listener Setup
description: Configure multiple simultaneous listeners for split-screen, multiplayer, and broadcast audio scenarios.
diataxis: how-to
---

This guide explains how to set up and manage multiple listeners in Amplitude. Multiple listeners are essential for split-screen multiplayer, broadcast cameras, and any scenario where more than one point of audition exists in the game world.

## Overview

By default, Amplitude creates one listener. You can create additional listeners and assign entities to specific listeners, allowing each listener to hear a tailored mix of the game audio.

## Engine Configuration

First, ensure the engine is configured to support multiple listeners:

```json
{
  "game": {
    "listener_fetch_mode": "Nearest",
    "listeners": 4
  }
}
```

| Option | Description |
|--------|-------------|
| `listeners` | Maximum number of simultaneous listeners. |
| `listener_fetch_mode` | How entities choose which listener to use: `Nearest` or `First`. |

### Listener Fetch Modes

| Mode | Behavior |
|------|----------|
| `None` | No listener is fetched; all audio is muted but processing continues. |
| `Nearest` | Each entity uses the closest listener for spatialization calculations. |
| `Farthest` | Each entity uses the farthest listener. |
| `Default` | All entities use the listener set via `Engine::SetDefaultListener()`. |
| `First` | All entities use the first registered listener. |
| `Last` | All entities use the last registered listener. |

## Creating Listeners

Create listeners at runtime after engine initialization:

```cpp
// Create two listeners for split-screen multiplayer
amEngine->AddListener(1); // Player 1
amEngine->AddListener(2); // Player 2

// Get handles
Listener player1 = amEngine->GetListener(1);
Listener player2 = amEngine->GetListener(2);
```

## Updating Listener Transforms

Update each listener's position and orientation every frame:

```cpp
// Player 1 (top half of screen)
player1.SetLocation(player1Position);
player1.SetOrientation(player1Orientation);

// Player 2 (bottom half of screen)
player2.SetLocation(player2Position);
player2.SetOrientation(player2Orientation);
```

## Per-Listener Settings

Each listener has its own spatial properties:

```cpp
// Set directivity for each listener
player1.SetDirectivity(0.5f, 2.0f);
player2.SetDirectivity(0.5f, 2.0f);
```

## Assigning Entities to Listeners

By default, the engine automatically assigns entities to the nearest listener based on `listener_fetch_mode`. You can override this behavior manually if needed by updating the entity's spatial relationship through the engine's internal state.

## Split-Screen Audio Example

A typical split-screen setup:

```cpp
void UpdateAudio()
{
    // Update listener transforms from game cameras
    listener1.SetLocation(camera1.GetPosition());
    listener1.SetOrientation(camera1.GetOrientation());

    listener2.SetLocation(camera2.GetPosition());
    listener2.SetOrientation(camera2.GetOrientation());

    // The engine automatically spatializes sounds for both listeners
    // and mixes them into the final output
}
```

## Output Routing

Amplitude mixes all listener outputs into a single stereo (or multi-channel) stream. If you need per-listener output to separate audio devices, you must run separate engine instances or implement a custom driver that routes channels accordingly.

## Performance Considerations

Each additional listener increases CPU cost because:

- Spatialization calculations run once per listener
- HRTF/Ambisonic decoding processes one stream per listener
- Bus mixing sums contributions from all listeners

For most games, 2–4 listeners is practical. For more than 4 listeners, consider using `BinauralMediumQuality` or `Stereo` panning modes to reduce CPU load.

## Removing Listeners

Clean up listeners when they are no longer needed:

```cpp
amEngine->RemoveListener(2);
```

## Next Steps

- Review the [Managing Game Objects](managing-game-objects.md) guide for entity setup.
- Learn about [Rooms and Environments](managing-game-objects.md#acoustic-spaces) to add acoustics to each listener's space.
