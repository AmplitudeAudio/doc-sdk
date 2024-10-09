---
title: The rendering loop
description: Amplitude has been built in a way it will adapt to your game framerate, through its update procedure.
---

Amplitude has been built in a way it will adapt to your game framerate. For that, any update to the internal state is done in a _rendering loop_ (which may be your main game loop), where you provide to the engine the time elapsed since the last update.

A typical rendering loop may look as this:

```cpp
// A rendering loop running at 60 FPS
while (true)
{
  if (!mIsRunning)
    break;

  // ... Update Amplitude state ...

  AmTime fps = 1.0 / 60.0; // Limit to 60 frames per seconds
  amEngine->AdvanceFrame(fps); // Apply the engine state updates
  Thread::Sleep(static_cast<AmInt32>(fps * kAmSecond)); // Wait for the next frame to start
}
```

In most of the cases, you will just need to place the `AdvanceFrame()` method somewhere in your game update procedure.

!!! tip
    The recommended place to update Amplitude is after the update of the physics system, and before the update of the render system.

Amplitude uses the `AdvanceFrame()` method is to update the internal state of various game objects such as entities, listeners, rooms, and environments, as well as fading state, playback status of running channels, and RTPC curves.
