---
title: Interacting with the Engine
description: Play sounds, update real-time parameters, change active switch states, and more through the Amplitude engine.
menu:
  docs:
    parent: integration
weight: 205
toc: true
---

!!! danger Incomplete Documentation
    This documentation page is WIP and not yet complete. You can have a complete demo on how to interact with the engine through the official [sample projects](https://github.com/AmplitudeAudio/sdk/blob/develop/samples).

## The rendering loop

Amplitude has been built in a way it will adapt to your game framerate. For that, any update to the internal state is
done in a _rendering loop_ (which may be your main game loop), where you provide to the engine the time elapsed since
the last update.

A typical rendering loop may look as this:

```cpp
// A rendering loop running at 60 FPS
while (true)
{
  if (!mIsRunning)
    break;

  // ... Update Amplitude state ...

  AmTime fps = 1.0 / 60.0;
  amEngine->AdvanceFrame(fps); // Apply the engine state updates
  Thread::Sleep(static_cast<AmInt32>(fps * kAmSecond));
}
```

This will help Amplitude to correctly process various timed updates like fading transitions and RTPC curves.