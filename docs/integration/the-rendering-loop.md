---
title: The Rendering Loop
description: Amplitude has been built in a way it will adapt to your game framerate, through its update procedure.
diataxis: how-to
---

Amplitude has been built in a way it will adapt to your game framerate. For that, any update to the internal state is done in a _rendering loop_ (which may be your main game loop), where you provide to the engine the time elapsed since the last update.

## Basic Integration

A typical rendering loop may look like this:

```cpp
// A rendering loop running at 60 FPS
while (true)
{
  if (!mIsRunning)
    break;

  // ... Update Amplitude state ...

  AmTime frameMs = kAmSecond / 60.0; // ~16.67 ms per frame at 60 FPS
  amEngine->AdvanceFrame(frameMs); // Apply the engine state updates (delta in milliseconds)
  Thread::Sleep(static_cast<AmInt32>(frameMs)); // Wait for the next frame to start
}
```

In most cases, you will just need to place the `AdvanceFrame()` method somewhere in your game update procedure.

!!! tip
    The recommended place to update Amplitude is after the update of the physics system, and before the update of the render system.

## What AdvanceFrame() Does

The `AdvanceFrame()` method is the heartbeat of the Amplitude engine. It updates the internal state of all audio systems in a specific order:

1. **Execute Pending Callbacks** — Any callbacks scheduled for the next frame are executed
2. **Cleanup Finished Sounds** — Completed sound playbacks are removed from the active list
3. **Sort Rooms by Volume** — Rooms are ordered by size (largest first) for processing priority
4. **Update RTPC Values** — All [Real-Time Parameter Control](../project/rtpc.md) values are updated based on elapsed time
5. **Update Effects** — Effect parameters are refreshed
6. **Update Spatial Objects** — Listeners, environments, and rooms recalculate their transforms and properties
7. **Update Entities** — Entity positions are updated and environment factors are recalculated (if automatic tracking is enabled)
8. **Update Bus Ducking** — Bus duck gains are reset and recalculated
9. **Process Audio** — The master bus advances, triggering the Amplimix pipeline to process audio
10. **Update Channels** — Spatial audio calculations, attenuation, and priority are computed for each active channel
11. **Sort Channels by Priority** — Channels are sorted to determine which play as real vs. virtual
12. **Update Voice Allocation** — Real and virtual channel assignments are updated based on priority
13. **Update Running Events** — Active events advance their state machines
14. **Increment Frame Counter** — The engine's frame counter and total time are updated

## Frame Timing

The `delta` parameter you pass to `AdvanceFrame()` represents the time elapsed since the last frame, **in milliseconds** (`AmTime` is `AmReal64`):

```cpp
// Using a fixed timestep
AmTime fixedDelta = kAmSecond / 60.0; // ~16.67 ms at 60 FPS
amEngine->AdvanceFrame(fixedDelta);

// Using actual elapsed time
AmTime actualDelta = timer.GetElapsedMilliseconds();
timer.Reset();
amEngine->AdvanceFrame(actualDelta);
```

!!! warning
    Passing inconsistent or very large delta values can cause audio artifacts or timing issues. For best results, use consistent frame timing or cap your delta value to a reasonable maximum (e.g., `kAmSecond / 30.0` ≈ 33 ms).

## Thread Safety

The `AdvanceFrame()` method is protected by an internal mutex, making it safe to call from any single thread. However, you should avoid calling it concurrently from multiple threads.

```cpp
// Safe: Single-threaded update
void GameLoop::Update(AmTime delta)
{
    // Update game systems...
    UpdatePhysics(delta);

    // Update Amplitude (safe - internal mutex protects state)
    amEngine->AdvanceFrame(delta);

    // Update rendering...
    RenderFrame();
}
```

!!! note
    While `AdvanceFrame()` is thread-safe, you should still synchronize your own code when accessing Amplitude objects (entities, listeners, etc.) from multiple threads.

## Recommended Update Order

For best results, integrate Amplitude into your game loop in this order:

```cpp
void GameLoop::Update(AmTime delta)
{
    // 1. Process input
    ProcessInput();

    // 2. Update game logic
    UpdateGameLogic(delta);

    // 3. Update physics
    UpdatePhysics(delta);

    // 4. Update Amplitude positions from game objects
    UpdateAudioPositions();  // Sync entity/listener positions

    // 5. Advance Amplitude frame
    amEngine->AdvanceFrame(delta);

    // 6. Render graphics
    RenderFrame();
}

void GameLoop::UpdateAudioPositions()
{
    // Update listener from camera
    Listener listener = amEngine->GetListener(1);
    listener.SetLocation(camera.GetPosition());
    listener.SetOrientation(Orientation(camera.GetForward(), camera.GetUp()));

    // Update entities from game objects
    for (auto& gameObject : gameObjects)
    {
        Entity entity = amEngine->GetEntity(gameObject.GetId());
        if (entity.Valid())
        {
            entity.SetLocation(gameObject.GetPosition());
            entity.SetOrientation(Orientation(gameObject.GetForward(), gameObject.GetUp()));
        }
    }
}
```

## Pausing the Engine

You can pause and resume the engine without stopping the game loop:

```cpp
// Pause all audio processing
amEngine->Pause(true);

// ... Game is paused but loop continues ...

// Resume audio processing
amEngine->Pause(false);
```

When paused, `AdvanceFrame()` will return early without processing audio, but your game loop can continue running normally.

## Performance Considerations

The `AdvanceFrame()` method performs significant work each frame:

- **Audio Processing** — DSP operations for all active sounds
- **Spatial Calculations** — 3D positioning, HRTF, and room acoustics
- **Priority Sorting** — Channel prioritization for voice management

For optimal performance:

- Keep the number of simultaneous sounds within your configured limits
- Use virtual channels (sounds that are too quiet or far away) to reduce processing load
- Consider using lower-complexity spatialization for less important sounds
- Profile your audio performance alongside graphics and physics

!!! tip
    The engine automatically virtualizes low-priority sounds when voice limits are reached. Virtual sounds continue to track position and timing but don't consume DSP resources.
